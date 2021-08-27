package routers

import (
	"digiapi/api/response"
	"digiapi/database/digimon"
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"

	"github.com/go-chi/chi"
)

// DigimonRouter uses the Repository to handle CRUD.
type DigimonRouter struct {
	Repository digimon.Repository
}

// CreateHandler creates a Digimon using the Repository.
func (dr *DigimonRouter) CreateHandler(w http.ResponseWriter, r *http.Request) {
	var d digimon.Model
	err := json.NewDecoder(r.Body).Decode(&d)
	if err != nil {
		response.HTTPError(w, r, http.StatusBadRequest, err.Error())
		return
	}

	defer r.Body.Close()

	ctx := r.Context()
	err = dr.Repository.Create(ctx, &d)
	if err != nil {
		response.HTTPError(w, r, http.StatusBadRequest, err.Error())
		return
	}

	w.Header().Add("Location", fmt.Sprintf("%s%d", r.URL.String(), d.ID))
	response.JSON(w, r, http.StatusCreated, response.Map{"digimon": d})
}

// GetAllHandler retrieves all the Digimons
func (dr *DigimonRouter) GetAllHandler(w http.ResponseWriter, r *http.Request) {
	ctx := r.Context()
	digimons := dr.Repository.GetAll(ctx)

	response.JSON(w, r, http.StatusOK, response.Map{"digimons": digimons})
}

// GetOneHandler retrieves a DigiFamilie by ID.
func (dr *DigimonRouter) GetOneHandler(w http.ResponseWriter, r *http.Request) {
	idStr := chi.URLParam(r, "id")

	id, err := strconv.Atoi(idStr)
	if err != nil {
		response.HTTPError(w, r, http.StatusBadRequest, err.Error())
		return
	}

	ctx := r.Context()
	d, err := dr.Repository.GetOne(ctx, uint(id))
	if err != nil {
		response.HTTPError(w, r, http.StatusNotFound, err.Error())
		return
	}

	response.JSON(w, r, http.StatusOK, response.Map{"digimon": d})
}

// UpdateHandler updated a Digimon.
func (dr *DigimonRouter) UpdateHandler(w http.ResponseWriter, r *http.Request) {
	idStr := chi.URLParam(r, "id")

	id, err := strconv.Atoi(idStr)
	if err != nil {
		response.HTTPError(w, r, http.StatusBadRequest, err.Error())
		return
	}

	var d digimon.Model
	err = json.NewDecoder(r.Body).Decode(&d)
	if err != nil {
		response.HTTPError(w, r, http.StatusBadRequest, err.Error())
		return
	}

	defer r.Body.Close()

	ctx := r.Context()
	err = dr.Repository.Update(ctx, uint(id), d)
	if err != nil {
		response.HTTPError(w, r, http.StatusNotFound, err.Error())
		return
	}

	response.JSON(w, r, http.StatusOK, nil)
}

// DeleteHandler deletes a Digimon.
func (dr *DigimonRouter) DeleteHandler(w http.ResponseWriter, r *http.Request) {
	idStr := chi.URLParam(r, "id")

	id, err := strconv.Atoi(idStr)
	if err != nil {
		response.HTTPError(w, r, http.StatusBadRequest, err.Error())
		return
	}

	ctx := r.Context()
	err = dr.Repository.Delete(ctx, uint(id))
	if err != nil {
		response.HTTPError(w, r, http.StatusNotFound, err.Error())
		return
	}

	response.JSON(w, r, http.StatusOK, response.Map{})
}

// Routes has the definition of all the digimon routes.
func (dr *DigimonRouter) Routes() http.Handler {
	r := chi.NewRouter()

	r.Get("/", dr.GetAllHandler)
	r.Post("/", dr.CreateHandler)
	r.Get("/{id}", dr.GetOneHandler)
	r.Put("/{id}", dr.UpdateHandler)
	r.Delete("/{id}", dr.DeleteHandler)

	return r
}

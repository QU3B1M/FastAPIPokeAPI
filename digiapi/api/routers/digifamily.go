package routers

import (
	"digiapi/api/response"
	"digiapi/database/digifamily"
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"

	"github.com/go-chi/chi"
)

// DigiFamilyRouter uses the Repository to handle CRUD.
type DigiFamilyRouter struct {
	Repository digifamily.Repository
}

// CreateHandler creates a DigiFamily using the Repository.
func (dfr *DigiFamilyRouter) CreateHandler(w http.ResponseWriter, r *http.Request) {
	var family digifamily.Model
	err := json.NewDecoder(r.Body).Decode(&family)
	if err != nil {
		response.HTTPError(w, r, http.StatusBadRequest, err.Error())
		return
	}

	defer r.Body.Close()

	ctx := r.Context()
	err = dfr.Repository.Create(ctx, &family)
	if err != nil {
		response.HTTPError(w, r, http.StatusBadRequest, err.Error())
		return
	}

	w.Header().Add("Location", fmt.Sprintf("%s%d", r.URL.String(), family.ID))
	response.JSON(w, r, http.StatusCreated, response.Map{"digifamily": family})
}

// GetAllHandler retrieves all the DigiFamilies
func (dfr *DigiFamilyRouter) GetAllHandler(w http.ResponseWriter, r *http.Request) {
	ctx := r.Context()
	families := dfr.Repository.GetAll(ctx)

	response.JSON(w, r, http.StatusOK, response.Map{"digifamilies": families})
}

// GetOneHandler retrieves a DigiFamilie by ID.
func (dfr *DigiFamilyRouter) GetOneHandler(w http.ResponseWriter, r *http.Request) {
	idStr := chi.URLParam(r, "id")

	id, err := strconv.Atoi(idStr)
	if err != nil {
		response.HTTPError(w, r, http.StatusBadRequest, err.Error())
		return
	}

	ctx := r.Context()
	family, err := dfr.Repository.GetOne(ctx, uint(id))
	if err != nil {
		response.HTTPError(w, r, http.StatusNotFound, err.Error())
		return
	}

	response.JSON(w, r, http.StatusOK, response.Map{"digifamily": family})
}

// UpdateHandler updated a DigiFamily.
func (dfr *DigiFamilyRouter) UpdateHandler(w http.ResponseWriter, r *http.Request) {
	idStr := chi.URLParam(r, "id")

	id, err := strconv.Atoi(idStr)
	if err != nil {
		response.HTTPError(w, r, http.StatusBadRequest, err.Error())
		return
	}

	var family digifamily.Model
	err = json.NewDecoder(r.Body).Decode(&family)
	if err != nil {
		response.HTTPError(w, r, http.StatusBadRequest, err.Error())
		return
	}

	defer r.Body.Close()

	ctx := r.Context()
	err = dfr.Repository.Update(ctx, uint(id), family)
	if err != nil {
		response.HTTPError(w, r, http.StatusNotFound, err.Error())
		return
	}

	response.JSON(w, r, http.StatusOK, nil)
}

// DeleteHandler deletes a DigiFamily.
func (dfr *DigiFamilyRouter) DeleteHandler(w http.ResponseWriter, r *http.Request) {
	idStr := chi.URLParam(r, "id")

	id, err := strconv.Atoi(idStr)
	if err != nil {
		response.HTTPError(w, r, http.StatusBadRequest, err.Error())
		return
	}

	ctx := r.Context()
	err = dfr.Repository.Delete(ctx, uint(id))
	if err != nil {
		response.HTTPError(w, r, http.StatusNotFound, err.Error())
		return
	}

	response.JSON(w, r, http.StatusOK, response.Map{})
}

// Routes has the definition of all the digifamily routes.
func (dfr *DigiFamilyRouter) Routes() http.Handler {
	r := chi.NewRouter()

	r.Get("/", dfr.GetAllHandler)
	r.Post("/", dfr.CreateHandler)
	r.Get("/{id}", dfr.GetOneHandler)
	r.Put("/{id}", dfr.UpdateHandler)
	r.Delete("/{id}", dfr.DeleteHandler)

	return r
}

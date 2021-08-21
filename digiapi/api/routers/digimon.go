package routers

import (
	"digiapi/database/digimon"
	"net/http"

	"github.com/go-chi/chi"
)

// DigimonRouter uses the Repository to handle CRUD.
type DigimonRouter struct {
	Repository digimon.Repository
}

// Routes has the definition of all the digimon routes.
func (dfr *DigimonRouter) Routes() http.Handler {
	r := chi.NewRouter()

	// r.Get("/", dfr.GetAllHandler)
	// r.Post("/", dfr.CreateHandler)
	// r.Get("/{id}", dfr.GetOneHandler)
	// r.Put("/{id}", dfr.UpdateHandler)
	// r.Delete("/{id}", dfr.DeleteHandler)

	return r
}

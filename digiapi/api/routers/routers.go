package routers

import (
	"digiapi/database"
	"digiapi/database/repository"
	"net/http"

	"github.com/go-chi/chi"
)

// New instance of the api routers.
func New() http.Handler {
	r := chi.NewRouter()

	digifamilyrouter := &DigiFamilyRouter{Repository: &repository.DigiFamily{DB: database.Connect()}}

	r.Mount("/digifamily", digifamilyrouter.Routes())

	return r
}

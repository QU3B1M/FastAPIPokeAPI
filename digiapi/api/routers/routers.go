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

	dfr := &DigiFamilyRouter{Repository: &repository.DigiFamily{DB: database.Connect()}}
	dr := &DigimonRouter{Repository: &repository.Digimon{DB: database.Connect()}}

	r.Mount("/family", dfr.Routes())
	r.Mount("/digimon", dr.Routes())

	return r
}

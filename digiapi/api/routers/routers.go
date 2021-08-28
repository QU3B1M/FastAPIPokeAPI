package routers

import (
	"digiapi/api/middleware"
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

	r.Use(middleware.Authorizator)
	r.Mount("/digifamily", dfr.Routes())
	r.Mount("/digimon", dr.Routes())

	return r
}

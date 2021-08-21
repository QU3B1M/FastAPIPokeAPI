package api

import (
	"digiapi/config"
	"log"
	"net/http"
	"time"

	"github.com/go-chi/chi"
)

// API is a base server configuration.
type API struct {
	server *http.Server
}

// New inicialize a new server with configuration.
func New() (*API, error) {
	r := chi.NewRouter()

	api := &http.Server{
		Addr:         ":" + config.Port,
		Handler:      r,
		ReadTimeout:  10 * time.Second,
		WriteTimeout: 10 * time.Second,
	}

	server := API{server: api}

	return &server, nil
}

// Close server resources.
func (api *API) Close() error {
	// TODO: add resource closure.
	return nil
}

// Start the server.
func (api *API) Start() {
	log.Print("Starting app")
	log.Printf("API running on http://localhost%s", api.server.Addr)
	// if !database.IsActive() {
	// 	log.Fatal("No DB Connection.")
	// 	return
	// }
	log.Fatal(api.server.ListenAndServe())

}

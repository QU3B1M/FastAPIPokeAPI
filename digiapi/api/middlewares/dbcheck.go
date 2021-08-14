package middlewares

import (
	"net/http"
	"digiapi/api/database"
)

// CheckDB verifies the database connection status.
func CheckDB(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if !database.IsActive() {
			http.Error(w, "DataBase Connection Lost", 500)
			return
		}
		next.ServeHTTP(w, r)
	}
}

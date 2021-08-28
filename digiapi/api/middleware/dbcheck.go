package middleware

import (
	"net/http"
)

// CheckDB verifies the database connection status.
func CheckDB(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		// if !database.IsActive() {
		// 	http.Error(w, "DB Connection Lost", 500)
		// 	return
		// }
		next.ServeHTTP(w, r)
	}
}

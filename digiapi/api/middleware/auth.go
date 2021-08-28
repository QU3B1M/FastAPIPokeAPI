package middleware

import (
	"digiapi/api/response"
	"digiapi/api/security"
	"digiapi/config"
	"errors"
	"net/http"
	"strings"
)

func authToken(authorization string) (string, error) {
	if authorization == "" {
		return "", errors.New("Autorization is required")
	}

	if !strings.HasPrefix(authorization, "Bearer") {
		return "", errors.New("Invalid autorization token")
	}

	l := strings.Split(authorization, " ")
	if len(l) != 2 {
		return "", errors.New("Invalid autorization token")
	}

	return l[1], nil
}

// Authorizator is a middleware that authorizes the user to the endpoints
func Authorizator(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		authorization := r.Header.Get("Authorization")
		tokenString, err := authToken(authorization)
		if err != nil {
			response.HTTPError(w, r, http.StatusUnauthorized, err.Error())
			return
		}

		_, err = security.DecodeToken(tokenString, config.SecretKey)
		if err != nil {
			response.HTTPError(w, r, http.StatusUnauthorized, err.Error())
			return
		}

		next.ServeHTTP(w, r)
	})
}

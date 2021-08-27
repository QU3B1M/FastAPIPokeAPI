package response

import (
	"encoding/json"
	"net/http"
)

// ErrorMessage standar body.
type ErrorMessage struct {
	Message string `json:"message"`
}

// Map will help us to serialize/deserialize data.
type Map map[string]interface{}

// JSON serializes the response data.
func JSON(w http.ResponseWriter, r *http.Request, statusCode int, data interface{}) error {
	if data == nil {
		w.Header().Set("Content-Type", "application/json; charset=utf-8")
		w.WriteHeader(statusCode)
		return nil
	}

	j, err := json.Marshal(data)
	if err != nil {
		return err
	}

	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	w.WriteHeader(statusCode)
	w.Write(j)
	return nil
}

// HTTPError creates a new ErrorMessage.
func HTTPError(w http.ResponseWriter, r *http.Request, statusCode int, message string) error {
	msg := ErrorMessage{
		Message: message,
	}

	return JSON(w, r, statusCode, msg)
}

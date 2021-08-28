package security

import (
	"errors"

	jwt "github.com/dgrijalva/jwt-go"
)

// Claim is our Token model
type Claim struct {
	jwt.StandardClaims
	Scope string `json:"scope"`
}

// DecodeToken and returns the Payload.
func DecodeToken(tokenString, secretKey string) (*Claim, error) {
	token, err := jwt.Parse(tokenString, func(*jwt.Token) (interface{}, error) {
		return []byte(secretKey), nil
	})
	if err != nil {
		return nil, err
	}
	if !token.Valid {
		return nil, errors.New("Invalid token")
	}

	claim, ok := token.Claims.(jwt.MapClaims)
	if !ok {
		return nil, errors.New("Invalid claim")
	}
	scope, ok := claim["scope"]
	if !ok {
		return nil, errors.New("Invalid scope")
	}
	if scope != "access_token" {
		return nil, errors.New("Invalid token")
	}
	return &Claim{}, nil
}

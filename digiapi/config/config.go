package config

import (
	"os"

	// _ its needed to get vars from .env if it exists
	_ "github.com/joho/godotenv/autoload"
)

// Config variables
var (
	DataBaseURL = os.Getenv("database_url")
	Port        = os.Getenv("port")
	APIPrefix   = os.Getenv("api_prefix")
	SecretKey   = os.Getenv("secret_key")
	// APIPrefix   = "/api/v1/digiapi"
	// SecretKey   = getEnv("SECRET_KEY")
	// JWTKey      = []byte(getEnv("JWT_KEY"))
	// SecretKey    = getEnv("SECRET_KEY")
	// JWTKey       = []byte(getEnv("JWT_KEY"))
)

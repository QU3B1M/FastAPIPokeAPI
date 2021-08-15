package config

import (
	"log"
	"os"

	"github.com/joho/godotenv"
)

var (
	DataBaseURL = "file::memory:?cache=shared"
	// Port        = getEnv("PORT")
	// SecretKey   = getEnv("SECRET_KEY")
	// JWTKey      = []byte(getEnv("JWT_KEY"))
	// DataBase_URL = getEnv("DATABASE_URL")
	// Port         = getEnv("PORT")
	// SecretKey    = getEnv("SECRET_KEY")
	// JWTKey       = []byte(getEnv("JWT_KEY"))
)

// getEnv Loads the .env file and reads the data
func getEnv(name string) string {
	err := godotenv.Load(".env")

	if err != nil {
		log.Fatalf("Error loading .env file")
	}
	env := os.Getenv(name)
	if env == "" {
		panic("failed to get env for " + name)
	}
	return env
}

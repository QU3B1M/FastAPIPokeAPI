package database

import (
	"digiapi/api/models"
	"digiapi/config"
	"log"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

// DataBase is an connected instance of the DataBase.
var DataBase = Connect()

// Ill use this when migrating to postgresql
// var dns = url.URL{
// 	User:     url.UserPassword(config.Settings.Postgres.User, config.Settings.Postgres.Password),
// 	Scheme:   "postgres",
// 	Host:     fmt.Sprintf("%s:%d", config.Settings.Postgres.Host, config.Settings.Postgres.Port),
// 	Path:     config.Settings.Postgres.DBName,
// 	RawQuery: (&url.Values{"sslmode": []string{"disable"}}).Encode(),
// }

// Connect establishes the connection to the DataBase.
func Connect() *gorm.DB {
	db, err := gorm.Open(sqlite.Open(config.DataBaseURL), &gorm.Config{})
	if err != nil {
		log.Fatal("Error while connecting to DataBase.")
		return db
	}
	log.Println("Connected to Database")
	return db
}

// IsActive checks the connection to the database
func IsActive() bool {
	if DataBase == nil {
		log.Fatal("DataBase Connection is lost.")
		return false
	}
	return true
}

// init Initializes the migrations
func init() {
	DataBase.AutoMigrate(&models.Digimon{}, &models.Family{})
}

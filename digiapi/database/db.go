package database

import (
	"digiapi/config"
	"digiapi/database/digifamily"
	"digiapi/database/digimon"
	"log"
	"sync"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

// DB is an connected instance of the DataBase.
var (
	db   *DB
	once sync.Once
)

// DB is an instance of the DataBase
type DB struct {
	Conn *gorm.DB
}

// var DB = Connect()

// Ill use this when migrating to postgresql
// var dns = url.URL{
// 	User:     url.UserPassword(config.Settings.Postgres.User, config.Settings.Postgres.Password),
// 	Scheme:   "postgres",
// 	Host:     fmt.Sprintf("%s:%d", config.Settings.Postgres.Host, config.Settings.Postgres.Port),
// 	Path:     config.Settings.Postgres.DBName,
// 	RawQuery: (&url.Values{"sslmode": []string{"disable"}}).Encode(),
// }

// Connect establishes the connection to the DB.
func Connect() *DB {
	once.Do(initDB)
	return db
}

// initDB initialize the db variable with the connection to the database.
func initDB() {
	// conn, err := gorm.Open(sqlite.Open(config.DataBaseURL), &gorm.Config{})
	conn, err := gorm.Open(postgres.Open(config.DataBaseURL), &gorm.Config{})
	if err != nil {
		log.Fatal("Error while connecting to DB.")
	}
	log.Println("Connected to Database")
	conn.AutoMigrate(&digimon.Model{}, &digifamily.Model{})
	db = &DB{Conn: conn}
}

// // IsActive checks the connection to the database
// func IsActive() bool {
// 	if DB.Conn == nil {
// 		log.Fatal("DB Connection is lost.")
// 		return false
// 	}
// 	return true
// }

package digifamily

import "gorm.io/gorm"

// Model is a GORM DataBase Model.
type Model struct {
	gorm.Model
	Name         string
	Abbreviation string
	Description  string
	Emblem       string
}

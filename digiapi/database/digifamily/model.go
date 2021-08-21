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

// Tabler sets the Model tablename.
type Tabler interface {
	TableName() string
}

// TableName overrides the table name used by Family to `families`
func (Model) TableName() string {
	return "families"
}

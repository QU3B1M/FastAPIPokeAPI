package digimon

import (
	"context"
)

// Repository handle the CRUD operations with Digimons.
type Repository interface {
	GetAll(ctx context.Context) []Model
	GetOne(ctx context.Context, id uint) (Model, error)
	GetByName(ctx context.Context, name string) (Model, error)
	Create(ctx context.Context, digimonIn *Model) error
	Update(ctx context.Context, id uint, digimonIn Model) error
	Delete(ctx context.Context, id uint) error
}

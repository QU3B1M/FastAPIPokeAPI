from typing import List
from fastapi import APIRouter

from api.repositories import PokemonRepository
from api.models import PokemonIn, PokemonOut

router = APIRouter(prefix="/pokemon", tags=["Pokemons"])


@router.get("/", response_model=List[PokemonOut])
async def get_all_pokemons():
    """
    ## Retrieves a Pokemon List.

    Path Parameters
    ---------------
        None

    Body Parameters
    ---------------
        None

    Returns
    -------
        List[Pokemon]
    """
    return await PokemonRepository.get_all()


@router.get("/{id}", response_model=PokemonOut)
async def get_pokemon(id: int):
    """
    ## Retrieves a Pokemon by ID.

    Path Parameters
    ---------------
        id: int                 Pokemon ID.

    Body Parameters
    ---------------
        None

    Returns
    -------

        id: int                 Pokemon ID.
        name: str               Name of the Pokemon.
        description: str        Description of the Pokemon
        types: List[PokeType]   Type/s of the Pokemon
        moves: List[PokeMove]   Move/s of the Pokemon

    """
    return await PokemonRepository.get(id=id)


@router.post("/create", response_model=PokemonOut)
async def create_pokemon(poke_in: PokemonIn):
    """
    ## Creates a Pokemon.

    Path Parameters
    ---------------
        None

    Body Parameters
    ---------------
        id: int                 Pokemon ID.
        name: str               Name of the Pokemon.
        description: str        Description of the Pokemon.
        types_id: List[int]     IDs of the Pokemon type/s.
        moves_id: List[int]     IDs of the Pokemon Move/s.


    Returns
    -------

        id: int                 Pokemon ID.
        name: str               Name of the Pokemon.
        description: str        Description of the Pokemon.
        types: List[PokeType]   Type/s of the Pokemon.
        moves: List[PokeMove]   Move/s of the Pokemon.

    """
    return await PokemonRepository.create(poke_in)


@router.put("/update/{id}", response_model=int)
async def update_pokemon(id: int, poke_in: PokemonIn):
    """
    ## Updates a Pokemon by ID.

    Path Parameters
    ---------------
        id:int                  Pokemon ID.

    Body Parameters
    ---------------
        id: int                 Pokemon ID.
        name: str               Name of the Pokemon.
        description: str        Description of the Pokemon.
        types_id: List[int]     IDs of the Pokemon type/s.
        moves_id: List[int]     IDs of the Pokemon Move/s.


    Returns
    -------
        status: int

    """
    return await PokemonRepository.update(poke_in, id=id)


@router.delete("/delete/{id}", response_model=bool)
async def delete_pokemon(id: int):
    """
    ## Deletes a Pokemon by ID.

    Path Parameters
    ---------------
        Pokemon ID.

    Body Parameters
    ---------------
        None

    Returns
    -------

        None

    """
    return await PokemonRepository.delete(id=id)

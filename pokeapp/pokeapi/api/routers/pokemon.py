from typing import List

from fastapi import APIRouter, HTTPException

from api.database.schemas import Pokemon
from api.models import PokemonIn, PokemonOut, PokemonUpdate
from api.repositories import PokemonRepository, PokeMoveRepository, PokeTypeRepository


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
    pokemon: Pokemon = await PokemonRepository.get(id=id)
    if not pokemon:  # Non existent pokemon.
        raise HTTPException(status_code=404, detail="Non-existent Pokemon.")
    return pokemon


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
    # The pokemon needs PokeTypes and PokeMoves.
    if not poke_in.types_ids:
        raise HTTPException("Every Pokemon needs a type.")
    if not poke_in.moves_ids:
        raise HTTPException("Every have at least one move.")
    # The PokeTypes and PokeMoves IDs should be valids.
    for id in poke_in.types_ids:
        if not await PokeTypeRepository.exists(id=id):
            raise HTTPException(f"The id {id} doenst belong to any existent poketype.")
    for id in poke_in.moves_ids:
        if not await PokeMoveRepository.exists(id=id):
            raise HTTPException(f"The id {id} doenst belong to any existent pokemove.")
    # Now lets Create the Pokemon.
    return await PokemonRepository.create(poke_in)


@router.put("/update/{id}", response_model=int)
async def update_pokemon(id: int, poke_in: PokemonUpdate):
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
    if not await PokemonRepository.exists(id=id):
        # Non-existent Pokemon, we cant update it :(... maybe it evolved he..
        raise HTTPException(status_code=404, detail="Non-existent Pokemon.")
    # Every id should be valid.
    for id in poke_in.types_to_add:
        if not await PokeTypeRepository.exists(id=id):
            raise HTTPException(f"The id {id} doenst belong to any existent poketype.")
    for id in poke_in.moves_to_add:
        if not await PokeMoveRepository.exists(id=id):
            raise HTTPException(f"The id {id} doenst belong to any existent pokemove.")
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
    if not await PokemonRepository.exists(id=id):
        # Non-existent Pokemon, there is no need to delete it ;).
        raise HTTPException(status_code=404, detail="Non-existent Pokemon.")
    return await PokemonRepository.delete(id=id)

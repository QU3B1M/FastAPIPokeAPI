from typing import List

from fastapi import APIRouter, HTTPException

from api.repositories import PokeTypeRepository
from api.models import PokeTypeIn, PokeTypeOut


router = APIRouter(prefix="/poketype", tags=["PokeTypes"])


@router.get("/", response_model=List[PokeTypeOut])
async def get_all_poketypes():
    """
    ## Retrieves a PokeType List.

    Path Parameters
    ---------------
        None

    Body Parameters
    ---------------
        None

    Returns
    -------
        List[PokeType]
    """
    return await PokeTypeRepository.get_all()


@router.get("/{id}", response_model=PokeTypeOut)
async def get_poketype(id: int):
    """
    ## Retrieves a PokeType by ID.

    Path Parameters
    ---------------
        id: int             PokeType ID.

    Body Parameters
    ---------------
        None

    Returns
    -------
        id: int             PokeType ID.
        name: str           Name of the PokeType.
        description: str    Description of the PokeType.

    """
    poketype: PokeTypeOut = await PokeTypeRepository.get(id=id)
    if not poketype:
        # Non-existent Poketype.
        raise HTTPException(status_code=404, detail="Poketype not found.")
    return poketype


@router.post("/create", response_model=PokeTypeOut)
async def create_poketype(poke_in: PokeTypeIn):
    """
    ## Creates a PokeType.

    Path Parameters
    ---------------
        None

    Body Parameters
    ---------------
        name: str           Name of the PokeType.
        description: str    Description of the PokeType.


    Returns
    -------
        id: int             PokeType ID.
        name: str           Name of the PokeType.
        description: str    Description of the PokeType.

    """
    return await PokeTypeRepository.create(poke_in)


@router.put("/update/{id}", response_model=int)
async def update_poketype(id: int, poke_in: PokeTypeIn):
    """
    ## Updates a PokeType by ID.

    Path Parameters
    ---------------
        id:int                                  PokeType ID.

    Body Parameters
    ---------------
        name: str           Name of the PokeType.
        description: str    Description of the PokeType.


    Returns
    -------
        status: int

    """
    if not await PokeTypeRepository.exists(id=id):
        # Non-existent Poketype, so we cant update.
        raise HTTPException(status_code=404, detail="Non-existent PokeType.")
    return await PokeTypeRepository.update(poke_in, id=id)


@router.delete("/delete/{id}", response_model=bool)
async def delete_poketype(id: int):
    """
    ## Deletes a PokeType by ID.

    Path Parameters
    ---------------
        PokeType ID.

    Body Parameters
    ---------------
        None

    Returns
    -------

        None

    """
    if not await PokeTypeRepository.exists(id=id):
        # Non-existent Poketype, so we cant delete.
        raise HTTPException(status_code=404, detail="Non-existent PokeType.")
    return await PokeTypeRepository.update(id=id)

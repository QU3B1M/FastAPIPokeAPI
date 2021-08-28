FROM golang:1.16

WORKDIR /app

# Download necessary Go modules
COPY go.mod ./
COPY go.sum ./
RUN go mod download

WORKDIR /code/

# Copy all the files
COPY . /code

RUN go build -o /digiapi

EXPOSE 8000

CMD [ "/digiapi" ]

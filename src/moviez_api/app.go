package main

import (
	"fmt"
	"database/sql"
	_ "github.com/mattn/go-sqlite3"
)

type App struct {
//	Router	*mux.Router
	DB		*sql.DB
}

func (a *App) Initialize(user, password, dbname string) {}

func (a *App) Run(addr string) {
	fmt.Printf("Running %s\n", addr)
}

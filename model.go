package main

import (
	"database/sql"
)

type movie struct {
	ID       int    `json:"id"`
	Title    string `json:"title"`
	Plot     string `json:"plot"`
	Year     int    `json:"year"`
	Genre    string `json:"genre"`
	Rating   int    `json:"rating"`

	// user specified data
	USummary string `json:"usummary"`
	URating  int    `json:"urating"`
	USeen    bool   `json:"useen"`
}

func (m *movie) getMovie(db *sql.DB) error {
	return db.QueryRow("SELECT title FROM movies WHERE id=$1",
		m.ID).Scan(&m.Title)
}

func getMovies(db *sql.DB, start, count int) ([]movie, error) {
	rows, err := db.Query(
		"SELECT id, title FROM movies")

	if err != nil {
		return nil, err
	}

	defer rows.Close()

	movies := []movie{}

	for rows.Next() {
		var m movie
		if err := rows.Scan(&m.ID, &m.Title); err != nil {
			return nil, err
		}
		movies = append(movies, m)
	}

	return movies, nil
}

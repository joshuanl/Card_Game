CC = g++
CFLAGS = -Wall

BIN = bin
LIB = lib
SRC = src

all: main

$(BIN)/Card.o: $(SRC)/Card.cpp $(LIB)/Card.h 
	$(CC) -c $(BIN)/Card.o $(SRC)/Card.cpp $(CFLAGS)

$(BIN)/Deck.o: $(SRC)/Deck.cpp $(LIB)/Deck.h $(LIB)/Card.h
	$(CC) -c -o $@ @< $(CFLAGS)

$(BIN)/Record.o: $(SRC)/Record.cpp $(LIB)/Record.h 
	$(CC) -c -o $@ $< $(CFLAGS)	

$(BIN)/Player.o: $(SRC)/Player.cpp $(LIB)/Deck.h $(LIB)/Record.h 	
	$(CC) -c -o $@ $< $(CFLAGS)

$(BIN)/main.o: $(SRC)/main.cpp $(BIN)/Deck.o $(BIN)/Card.o $(BIN)/Player.o
	$(CC) -c -o $@ $< $(CFLAGS)

$(BIN)/main: $(BIN)/main.o $(BIN)/Deck.o $(BIN)/Card.o $(BIN)/Player.o 
	$(CC) -o $@ main.cpp main.o Deck.o Card.o $(CFLAGS)

.PHONY: clean

clean:	
	rm -rf $(BIN)/*
#include "Deck.h"
#include <stdlib.h>     
#include <time.h>       

using namespace std;

Deck::Deck(string name){
	size = 0;
	deck_name = name;
	cardBack = "BASIC";
	index = 0;
}//end of costructor
Deck::~Deck(){
	delete deck_of_cards;
}//end of destructor

void Deck::shuffle(){
	srand (time(NULL));
	int random_index, temp;
	for (int i = 0; i < deck_of_cards.size(); i++){
		random_index = rand() % deck_of_cards.size();
		Card temp_card(deck_of_cards[i]);
		deck_of_cards[i] = deck_of_cards[random_index];
		deck_of_cards[random_index] = temp_card;
	}//end of for
}//end of shuffle

Card Deck::draw() const;{
	index++;
	return deck_of_cards[(index-1)];
}//end of draw

void Deck::addCard(const Card card){
	deck_of_cards.push_back(card);
}//end of add a card

void Deck::removeCard(const int pos){
	deck_of_cards.erase(deck_of_cards.begin(), deck_of_cards.begin()+(pos-1));
}//end of removing card

void Deck::next(int amt){
	index += amt;       //check if out of bounds
}//end of next

void Deck::first(){
	index = 0;
}//end of first

int Deck::size() const{
	return size;
}//end of returning size of deck

int Deck::sizeInGame() const{
	return sizeInGame;
}//end of size of deck in game

const string Deck::getName() const{
	return deck_name;
}//end of get name
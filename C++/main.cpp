#include "lib/Player.h" //player includes deck -> card and record
#include "lib/Deck.h"
#include "lib/Card.h"
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[]){
	string user_input;
	string temp;
	bool accept = false;


	cout << "Game start" << endl;
	cout << "making new deck..." << endl;
	cout << "deckname: ";
	cin >> user_input;
	Deck deck1(user_input);
	temp = "attack";
	Card *temp_card = new Card(101, temp);
	deck1.addCard(*temp_card);
	cout << "deck1 size: " << deck1.getSize();
	temp = "attack, attack";
	temp_card = new Card(211, temp);
	deck1.addCard(*temp_card);
	cout << "deck1 size: " << deck1.getSize();
	temp = "heal, attack";
	temp_card = new Card(231, temp);
	deck1.addCard(*temp_card);
	cout << "deck1 size: " << deck1.getSize();
	cout << "deckame: " << deck1.getName() << endl << endl;

	temp_card = new Card(deck1.draw());
	temp_card->printCard();
	temp_card = new Card(deck1.draw());
	temp_card->printCard();
	temp_card = new Card(deck1.draw());
	temp_card->printCard();

	deck1.first();
	deck1.shuffle();

	temp_card = new Card(deck1.draw());
	temp_card->printCard();
	temp_card = new Card(deck1.draw());
	temp_card->printCard();
	temp_card = new Card(deck1.draw());
	temp_card->printCard();

	return 0;
}


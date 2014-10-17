#include "lib/Player.h" //player includes deck -> card and record
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[]){
	string user_input;
	bool accept = false;


	cout << "Game start" << end;
	cout << "making new deck..." << endl;
	cout << "deckname: ";
	cin >> user_input;
	Deck deck1(user_input);
	Card temp_card(101, "attack");
	deck1.addCard(temp_card);
	cout << "deck1 size: " << deck1.size();
	Card temp_card(211, "attack, attack");
	deck1.addCard(temp_card);
	cout << "deck1 size: " << deck1.size();
	Card temp_card(231, "heal, attack");
	deck1.addCard(temp_card);
	cout << "deck1 size: " << deck1.size();
	cout << "deckame: " << deck1.getName() << endl << endl;

	temp_card(deck1.draw());
	temp_card.printCard();
	temp_card(deck1.draw());
	temp_card.printCard();
	temp_card(deck1.draw());
	temp_card.printCard();

	deck1.first();
	deck1.shuffle();

	temp_card(deck1.draw());
	temp_card.printCard();
	temp_card(deck1.draw());
	temp_card.printCard();
	temp_card(deck1.draw());
	temp_card.printCard();


	return 0;
}


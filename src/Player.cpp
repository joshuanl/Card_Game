#include "lib/Player.h"
#include <iostream>

using namespace std;


Player::Player(string username, string password, int age){
	this->username = username;
	this->password = password
	this->age = age;
	createProfile();
}//end of constructor 

Player::~Player(){
	delete [] decklist;
	delete [] record;
}//end of destructor;

void Player::createProfile(){
	cout << "Creating your profile..." << endl;
	cout << "Name: ";
	cin >> name;
	cout << "Email address: ";
	cin >> email;
	cout << "Age: ";
	cin >> age;
	cout << "Country: ";
	cin >> country;
	cout << endl << "Security Question..." << endl;
	cout << "Enter a secret question.  You will be asked this question in case you forgret your username or password.";
	cout << ">> ";
	cin >> secret_question;
	cout << "Next provide the answer for your question (case sensitive)." << endl;
	cout << ">> ";
	cin >> secret_question_answer;
	cout << endl << "Finished creating your profile!" << endl << endl;
}//end of creating profile
void Player::changeQuestion(){
	string input, input2, input3;
	bool accept = false;
	cout << "  >> Changing Security Question <<" << endl;
	cout << "Please answer your original question first" << endl;
	cout << getQuestion() << endl:
	cout << ">> ";
	cin >> input;
	if (input != answer){
		cout << " >> Your answer was incorrect! <<" << endl;
	}
	else{
		while(!accept){
			cout << "Enter your new security question: ";
			cin >> input;
			cout << "Enter the new answer: ";
			cin >> input2;
			cout << "Reenter the password to verify: ";
			cin >> input3;
			if (input2 != input3){
				cout << " >> Passwords do not match! << " << endl;
			}
			else if (input2 == input3){
				secret_question = input;
				secret_question_answer = input2;
				accept = true;
			}
		}//end of while	
	}//end of else
}//end of change question

const string Player::getQuestion() const{
	return secret_question;
}// end of get question

const string Player::getAnswer() const{
	return secret_question_answer;
}//end of get answer

vector<Deck> Player::getDecklist() const{
	return decklist;
}//end of returning decklist

stack<Record> Player::getRecord() const{
	return record;
}//end of returning the record

void Player::changeDeckListSize(const int newSize){
	decklist_max_size = newSize;
}//end of changing max 

int Player::currentDecklistSize(){
	return decklist_current_size;
}//end of current deck list size

void Player::removeDeck(int pos){
	cout << " >> Deleted deck \"" + decklist[pos].getName() + "\"! << " << endl;
	decklist.erase(decklist.begin(), decklist.begin()+pos);
}//end of remove deck

void Player::addDeck(Deck deck){
	decklist.push_back(deck);
}//end of add deck
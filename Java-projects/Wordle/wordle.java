//We will store the words from words.txt in an array list
//Need this to read the words.txt file
import java.util.*; //need collections for randomization using shuffle 
import java.io.File; //going to be reading words.txt so need this
import java.io.FileNotFoundException; //Just incase someone deletes words.txt, I will try and catch it

public class wordle{

    public static final String resetColour = "\u001B[0m"; //string that colours the following text back to white
    public static final String yellow = "\u001B[33m"; //string that colours the following text yellow
    public static final String green = "\u001B[32m"; //string that colours the following text green

    public ArrayList<String> getWords(){ //This method reads words.txt and extracts each of the words between the commas
        ArrayList<String> words = new ArrayList<String>(); //make the array for the words in words.txt
        try {
            File wordFile = new File("C:/Users/ajbro/OneDrive/Documents/2024-Break-Projects/Java-projects/Wordle/words.txt"); //This will work for me but you will need to specify your path to "words.txt"
            Scanner readWords = new Scanner(wordFile); 
            while (readWords.hasNextLine()){
                String wordData = readWords.nextLine(); //get the line from the word file
                String tempWord = new String(); //This will be used in the following code that will read from the lines extracted
                for (int i = 0; i < wordData.length(); i++){ //Add characters to tempWord from the lines until a comma is seen, then add the tempWord to the array and empty tempWord
                    if (wordData.charAt(i) == ','){
                        words.add(tempWord);
                        tempWord = "";
                    }
                    else{
                        tempWord += wordData.charAt(i);
                    }
                }
                words.add(tempWord); //need to add the final word as it won't have a comma after it
            }
            readWords.close();
        }
        catch (FileNotFoundException error){ //If words.txt doesn't exist, throw and error message to help the player understand what went wrong
            System.out.println("ERROR: words.txt not found, cannot play the game");
        }
        return(words);
    }

    public String chooseRandomWord(ArrayList<String> words){ //This method will randomly choose a word from the previous array to use in the game
        String chosenWord = new String(); //string where we will store the word
        Collections.shuffle(words); //Shuffle the list so we can randomly choose a word
        chosenWord = words.get(0); //Since we shuffled, the first word is random
        return chosenWord; //return the random word
    }

    public ArrayList<String> makeBaseGuessesArray(String chosenWord){ //This hides the word with '-' characters then returns the base gameboard for the user
        String hiddenWord = new String(); //will be used to hide the word
        ArrayList<String> gameDisplay = new ArrayList<String>(); //will be used to keep the guesses so the player can use prior guesses for future refernce
        for (int i = 0; i < chosenWord.length(); i++){ //loop to make a string to hide the word
            hiddenWord += '-';
        }
        for (int i = 0; i < 6; i++){ //loop to add the newly hidden word to an array
            gameDisplay.add(hiddenWord);
        }
        return gameDisplay;
    }

    public ArrayList<String> updateGameboard(ArrayList<String> gameboard, String guess, int index){ //Changes the gameboard to include the new guess
        gameboard.set(index, guess);
        return gameboard;
    }

    public String updateCharacterColours(String guess, String hiddenWord){ //Like in wordle, this method gives colour coded feedback to the player based on characters in their guess
        String finalGuess = new String(); //creating a string which will be the colour coded version of the guess
        for (int i = 0; i < guess.length(); i++){ //going through each character in the guess
            if (hiddenWord.length() > i){ //This needs to be here to prevent index out of bounds errors
                if (guess.charAt(i) == hiddenWord.charAt(i)){ //If the character in the guess is right, colour it green in the colour coded version of the string
                    finalGuess += green + guess.charAt(i) + resetColour;
                }
                else if (hiddenWord.indexOf(guess.charAt(i)) != -1){ //If the guessed character is in the string but not in the right position, colour it yellow in the colour coded verison of the string
                    finalGuess += yellow + guess.charAt(i) + resetColour;
                }
                else{ //Don't colour if not in the string
                    finalGuess += guess.charAt(i);
                }
            }
            else { //if the guess is larger than the word, the characters after the length of the right word can't be in the right position, so only check if they are the right characters, not the position
                if (hiddenWord.indexOf(guess.charAt(i)) != -1){ //if the character is the word players are meant to be guessing
                    finalGuess += yellow + guess.charAt(i) + resetColour;
                }
                else{ //if the character is not in the word the player is guessing, don't colour it
                    finalGuess += guess.charAt(i);
                }
            }
        }
        return finalGuess;
    }

    public void displayGame(ArrayList<String> guesses){ //This will be used to allow the player to see the state of the game
        for (int i = 0; i < guesses.size(); i++){ //for each guess the player can make, this sets up the a string to print
            String setupString = "Guess ";
            setupString += Integer.toString(i);
            setupString += ": ";
            setupString += guesses.get(i);
            System.out.println(setupString);
        }
    }

    public static void main(String[] args){
        wordle game = new wordle(); //Initialise an instance of the game
        ArrayList<String> wordList = game.getWords(); //Use the method made earlier to get words from words.txt and store them in an array
        String hiddenWord = game.chooseRandomWord(wordList); //store the word the player will be guessing at in a string. Gotten from the method made earlier
        ArrayList<String> gameboard = game.makeBaseGuessesArray(hiddenWord); //make the gameboard using the method made earlier to allow the player to see the game

        System.out.println("Hi, welcome to Wordle");

        Scanner gameScanner = new Scanner(System.in); //needed to take the users inputs later

        for (int i = 0; i < 6; i++){ //The user gets 6 guesses so will loop that many times
            game.displayGame(gameboard); //display the gameboard for the player
            System.out.println("Please guess the word"); //prompt the player to imput a guess
            String guess = gameScanner.nextLine(); //get the players input
            if (guess.equals(hiddenWord)){ //if the player is right
                System.out.println("\n");
                System.out.println(green + "Woop woop, the word was '" + hiddenWord + "'" + resetColour); 
                guess = green + guess + resetColour; //skipping using the previous method to reduce complexity as we know the word should be all green
                game.updateGameboard(gameboard, guess, i); //update the board for later
                break; //get out of the loop as the player has won so doesn't need to guess anymore
            }
            else{ //if the guess isn't 100% right, need to give feedback to the player
                System.out.println("\n");
                guess = game.updateCharacterColours(guess, hiddenWord); //use the previous method to make a string to give feedback to the player
                game.updateGameboard(gameboard, guess, i); //update the board for later
            }
        }

        gameScanner.close(); //need to close the scanner after I am done with it
        game.displayGame(gameboard); //Show the gameboard after the game ends
    }
}
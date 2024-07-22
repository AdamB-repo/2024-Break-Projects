import java.util.ArrayList; //We will store the words from words.txt in an array list
import java.util.*; //need collections for randomization using shuffle 
import java.io.File; //going to be reading words.txt so need this
import java.io.FileNotFoundException; //Just incase someone deletes words.txt, I will try and catch it
import java.util.Scanner; //Need this to read the words.txt file

public class wordle{

    public ArrayList<String> getWords(){
        ArrayList<String> words = new ArrayList<String>(); //make the array for the words in words.txt
        try {
            File wordFile = new File("C:/Users/ajbro/OneDrive/Documents/2024-Break-Projects/Java-projects/Wordle/words.txt"); //This will work for me but you will need to specify your path to "words.txt"
            Scanner readWords = new Scanner(wordFile);
            while (readWords.hasNextLine()){
                String wordData = readWords.nextLine();
                String tempWord = new String();
                for (int i = 0; i < wordData.length(); i++){
                    if (wordData.charAt(i) == ','){
                        System.out.println(tempWord);
                        words.add(tempWord);
                        tempWord = "";
                    }
                    else{
                        tempWord += wordData.charAt(i);
                    }
                }
                System.out.println(tempWord);
                words.add(tempWord);
            }
            readWords.close();
        }
        catch (FileNotFoundException error){
            System.out.println("ERROR: words.txt not found, cannot play the game");
        }
        return(words);
    }

    public String chooseRandomWord(ArrayList<String> words){
        String chosenWord = new String();
        Collections.shuffle(words);
        chosenWord = words.get(0);
        return chosenWord;
    }

    public static void main(String[] args){
        wordle game = new wordle();
        ArrayList<String> wordList = game.getWords();
        String hiddenWord = game.chooseRandomWord(wordList);
        System.out.println(hiddenWord);
    }
}
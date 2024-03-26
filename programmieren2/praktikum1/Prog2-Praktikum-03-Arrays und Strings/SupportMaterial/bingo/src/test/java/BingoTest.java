import static org.junit.Assert.*;

import java.util.Arrays;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import org.junit.*;

public class BingoTest {


  /*
  @Test
  public void testBingoExample(){
    assertNotNull("BINGO_EXAMPLE must not be null", Bingo.BINGO_EXAMPLE);
    assertEquals("BINGO_EXAMPLE must contain exactly 5 rows ", 5, Bingo.BINGO_EXAMPLE.length);
    assertEquals("BINGO_EXAMPLE[0] must contain exactly 5 columns ", 5, Bingo.BINGO_EXAMPLE[0].length);
    assertEquals("BINGO_EXAMPLE[1] must contain exactly 5 columns ", 5, Bingo.BINGO_EXAMPLE[1].length);
    assertEquals("BINGO_EXAMPLE[2] must contain exactly 5 columns ", 5, Bingo.BINGO_EXAMPLE[2].length);
    assertEquals("BINGO_EXAMPLE[3] must contain exactly 5 columns ", 5, Bingo.BINGO_EXAMPLE[3].length);
    assertEquals("BINGO_EXAMPLE[4] must contain exactly 5 columns ", 5, Bingo.BINGO_EXAMPLE[4].length);

    assertEquals("expected  4 at Bingo.BINGO_EXAMPLE[0][0]",  4, Bingo.BINGO_EXAMPLE[0][0]);
    assertEquals("expected 27 at Bingo.BINGO_EXAMPLE[0][1]", 27, Bingo.BINGO_EXAMPLE[0][1]);
    assertEquals("expected 32 at Bingo.BINGO_EXAMPLE[0][2]", 32, Bingo.BINGO_EXAMPLE[0][2]);
    assertEquals("expected 55 at Bingo.BINGO_EXAMPLE[0][3]", 55, Bingo.BINGO_EXAMPLE[0][3]);
    assertEquals("expected 73 at Bingo.BINGO_EXAMPLE[0][4]", 73, Bingo.BINGO_EXAMPLE[0][4]);
    assertEquals("expected 15 at Bingo.BINGO_EXAMPLE[1][0]", 15, Bingo.BINGO_EXAMPLE[1][0]);
    assertEquals("expected 25 at Bingo.BINGO_EXAMPLE[1][1]", 25, Bingo.BINGO_EXAMPLE[1][1]);
    assertEquals("expected 41 at Bingo.BINGO_EXAMPLE[1][2]", 41, Bingo.BINGO_EXAMPLE[1][2]);
    assertEquals("expected 58 at Bingo.BINGO_EXAMPLE[1][3]", 58, Bingo.BINGO_EXAMPLE[1][3]);
    assertEquals("expected 75 at Bingo.BINGO_EXAMPLE[1][4]", 75, Bingo.BINGO_EXAMPLE[1][4]);
    assertEquals("expected  8 at Bingo.BINGO_EXAMPLE[2][0]",  8, Bingo.BINGO_EXAMPLE[2][0]);
    assertEquals("expected 26 at Bingo.BINGO_EXAMPLE[2][1]", 26, Bingo.BINGO_EXAMPLE[2][1]);
    assertEquals("expected 0, at Bingo.BINGO_EXAMPLE[2][2]",  0, Bingo.BINGO_EXAMPLE[2][2]);
    assertEquals("expected 59 at Bingo.BINGO_EXAMPLE[2][3]", 59, Bingo.BINGO_EXAMPLE[2][3]);
    assertEquals("expected 70 at Bingo.BINGO_EXAMPLE[2][4]", 70, Bingo.BINGO_EXAMPLE[2][4]);
    assertEquals("expected  7 at Bingo.BINGO_EXAMPLE[3][0]",  7, Bingo.BINGO_EXAMPLE[3][0]);
    assertEquals("expected 22 at Bingo.BINGO_EXAMPLE[3][1]", 22, Bingo.BINGO_EXAMPLE[3][1]);
    assertEquals("expected 33 at Bingo.BINGO_EXAMPLE[3][2]", 33, Bingo.BINGO_EXAMPLE[3][2]);
    assertEquals("expected 54 at Bingo.BINGO_EXAMPLE[3][3]", 54, Bingo.BINGO_EXAMPLE[3][3]);
    assertEquals("expected 63 at Bingo.BINGO_EXAMPLE[3][4]", 63, Bingo.BINGO_EXAMPLE[3][4]);
    assertEquals("expected 13 at Bingo.BINGO_EXAMPLE[4][0]", 13, Bingo.BINGO_EXAMPLE[4][0]);
    assertEquals("expected 17 at Bingo.BINGO_EXAMPLE[4][1]", 17, Bingo.BINGO_EXAMPLE[4][1]);
    assertEquals("expected 43 at Bingo.BINGO_EXAMPLE[4][2]", 43, Bingo.BINGO_EXAMPLE[4][2]);
    assertEquals("expected 48 at Bingo.BINGO_EXAMPLE[4][3]", 48, Bingo.BINGO_EXAMPLE[4][3]);
    assertEquals("expected 67 at Bingo.BINGO_EXAMPLE[4][4]", 67, Bingo.BINGO_EXAMPLE[4][4]);

  }*/

  /*@Test
  public void testContainsDuplicates(){

    assertFalse("must return false on bingo card without duplicats",
        Bingo.containsDuplicates(example));

    example[4][0] = 4;
    assertTrue("must return true on bingo card with duplicates",
        Bingo.containsDuplicates(example));
    example[4][0] = 13;

    example[4][0] = 0;
    assertFalse("must return false on bingo card with duplicate filled entries (0s)",
        Bingo.containsDuplicates(example));


  }*/

  /*@Test
  public void testCheckBingoCard(){

    assertThrows("null not allowed",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(null));

    assertThrows("no rows not allowed",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(new int[0][5]));

    assertThrows("three rows not allowed",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(new int[3][5]));

    assertThrows("more than 5 rows not allowed",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(new int[8][5]));

    assertThrows("no empty columns allowed",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(new int[5][0]));

    assertThrows("columns must have 5 entries",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(new int[5][4]));

    assertThrows("columns must have 5 entries",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(new int[5][8]));

    int[][] bingoCard = new int[5][5];
    bingoCard[3] = null;

    assertThrows("no null column allowed",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(new int[5][8]));

    example[2][2] = 42;
    assertThrows("middle field must be empty",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(example));
    example[2][2] = 0;

    example[3][4] = 88;
    assertThrows("value of 88 is invalid",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(example));

    example[3][4] = -5;
    assertThrows("value of -5 is invalid",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(example));

    example[3][4] = 63;

    example[2][0] = 16;
    assertThrows("value of 16 is invalid in first column",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(example));
    example[2][0] = 8;

    example[2][1] = 8;
    assertThrows("value of 8 is invalid in second column",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(example));
    example[2][1] = 26;

    example[4][2] = 61;
    assertThrows("value of 61 is invalid in third column",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(example));
    example[4][2] = 43;

    example[1][3] = 1;
    assertThrows("value of 1 is invalid in fourth column",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(example));
    example[1][3] = 58;

    example[3][4] = 32;
    assertThrows("value of 32 is invalid in fifth column",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(example));
    example[3][4] = 63;

    example[4][1] = 25;
    assertThrows("second column must not contain 25 twice",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(example));
    example[4][1] = 17;

    example[0][4] = 70;
    assertThrows("second column must not contain 25 twice",
        IllegalArgumentException.class,
        () -> Bingo.checkBingoCard(example));
    example[0][4] = 73;
  }*/

  /*@Test
  public void testFillBingoCard(){

    assertThrows("number must not be 0",
        IllegalArgumentException.class,
        () -> Bingo.fillBingoCard(example, 0));

    assertThrows("number must not be negative",
        IllegalArgumentException.class,
        () -> Bingo.fillBingoCard(example, -5));

    assertThrows("number must not be greater than 75",
        IllegalArgumentException.class,
        () -> Bingo.fillBingoCard(example, 76));

    assertTrue("must return true on found number",
        Bingo.fillBingoCard(example, 48));
    assertEquals("last row, fourth column must be empty (contained 48)",
        0, example[4][3]);

    assertTrue("must return true on found number",
        Bingo.fillBingoCard(example, 15));
    assertEquals("second row, first column must be empty (contained 15)",
        0, example[1][0]);

    assertFalse("must return false on number not on the card",
        Bingo.fillBingoCard(example, 60));

  }*/

  /*@Test
  public void testBingo(){

    assertFalse("must return false on no Bingo!",
        Bingo.bingo(example));

    init();
    for (int i = 0; i < 4; i++){
      example[i][3] = 0;
      assertFalse("must return false on no Bingo!",
          Bingo.bingo(example));
    }
    example[4][3] = 0;
    assertTrue("must return true on Bingo! (column)",
        Bingo.bingo(example));

    init();
    for (int i = 0; i < 4; i++){
      example[1][i] = 0;
      assertFalse("must return false on no Bingo!",
          Bingo.bingo(example));
    }
    example[1][4] = 0;
    assertTrue("must return true on Bingo! (row)",
        Bingo.bingo(example));

    init();
    for (int i = 0; i < 4; i++){
      example[i][i] = 0;
      assertFalse("must return false on no Bingo!",
          Bingo.bingo(example));
    }
    example[4][4] = 0;
    assertTrue("must return true on Bingo! (diagonal)",
        Bingo.bingo(example));

    init();
    for (int i = 0; i < 4; i++){
      example[i][4-i] = 0;
      assertFalse("must return false on no Bingo!",
          Bingo.bingo(example));
    }
    example[4][0] = 0;
    assertTrue("must return true on Bingo! (other diagonal)",
        Bingo.bingo(example));

  }*/




  private int[][] example;

  @Before
  public void init(){
    example = new int[5][5];
    example[0][0] =  4;
    example[0][1] = 27;
    example[0][2] = 32;
    example[0][3] = 55;
    example[0][4] = 73;
    example[1][0] = 15;
    example[1][1] = 25;
    example[1][2] = 41;
    example[1][3] = 58;
    example[1][4] = 75;
    example[2][0] =  8;
    example[2][1] = 26;
    example[2][2] =  0;
    example[2][3] = 59;
    example[2][4] = 70;
    example[3][0] =  7;
    example[3][1] = 22;
    example[3][2] = 33;
    example[3][3] = 54;
    example[3][4] = 63;
    example[4][0] = 13;
    example[4][1] = 17;
    example[4][2] = 43;
    example[4][3] = 48;
    example[4][4] = 67;
  }


}

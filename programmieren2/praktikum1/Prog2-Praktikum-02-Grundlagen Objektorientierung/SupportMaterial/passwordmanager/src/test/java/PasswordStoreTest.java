import org.junit.*;

import static org.junit.Assert.*;

public class PasswordStoreTest{

  /*private PasswordEntry e1;
  private PasswordEntry e2;
  private PasswordEntry e3;

  @Before
  public void init(){
    e1 = new PasswordEntry("moodle.haw-landshut.de", "s-cauer", PasswordComplexity.MEDIUM);
    e2 = new PasswordEntry("github.com", "java-programmer", PasswordComplexity.SIMPLE);
    e3 = new PasswordEntry("reddit.com", "extremelurker", PasswordComplexity.SUPER_COMPLEX);
  }

  @Test
  public void testConstructor(){

    PasswordStore store = new PasswordStore();
    assertEquals("empty password store has size 0", 0, store.getSize());
    assertEquals("empty password store has no first entry", null, store.getFirstEntry());

  }*/

  /*@Test
  public void testContains(){

    PasswordStore store = new PasswordStore();
    store.add(e3);
    store.add(e2);
    store.add(e1);
    e1 = new PasswordEntry("moodle.haw-landshut.de", "s-cauer", PasswordComplexity.MEDIUM);
    e2 = new PasswordEntry("github.com", "java-programmer",PasswordComplexity.SIMPLE);
    e3 = new PasswordEntry("reddit.com", "extremelurker", PasswordComplexity.SUPER_COMPLEX);

    assertTrue("must return true for e1", store.contains(e1));
    assertTrue("must return true for e2", store.contains(e2));
    assertTrue("must return true for e3", store.contains(e3));

    assertFalse("must return false for entry not in store", store.contains(new PasswordEntry("gitlab.com", "supercoder", PasswordComplexity.SUPER_COMPLEX)));

    assertThrows("null is not allowed as argument",
        IllegalArgumentException.class,
        () -> store.contains(null));

  }*/

  /*@Test
  public void testAdd(){

    PasswordStore store = new PasswordStore();

    assertTrue("must return false on e1", store.add(e1));
    assertEquals("size must be 1", 1, store.getSize());
    assertSame("first entry must be set", e1, store.getFirstEntry());
    assertNull("next entry of first entry must be null", e1.getNextEntry());

    assertTrue("must return false on e2", store.add(e2));
    assertEquals("size must be 2", 2, store.getSize());
    assertSame("first entry must be e2", e2, store.getFirstEntry());
    assertSame("next entry of first entry must be e1", e1, e2.getNextEntry());
    assertNull("next entry of second entry must be null", e1.getNextEntry());

    assertTrue("must return false on e3", store.add(e3));
    assertEquals("size must be 3", 3, store.getSize());
    assertSame("first entry must be e3", e3, store.getFirstEntry());
    assertSame("next entry of first entry must be e2", e2, e3.getNextEntry());
    assertSame("next entry of second entry must be e1", e1, e2.getNextEntry());
    assertNull("next entry of third entry must be null", e1.getNextEntry());

    assertThrows("null entry is invalid",
        IllegalArgumentException.class,
        () -> store.add(null));

    assertFalse("must return false when instance equal to e2 is added again", 
        store.add(new PasswordEntry("moodle.haw-landshut.de", "s-cauer", PasswordComplexity.MEDIUM)));

  }*/

  /*@Test
  public void testGet(){
    PasswordStore store = new PasswordStore();

    store.add(e3);
    store.add(e2);
    store.add(e1);

    assertSame("e1 must be at index 0", e1, store.get(0));
    assertSame("e2 must be at index 1", e2, store.get(1));
    assertSame("e3 must be at index 2", e3, store.get(2));

    assertThrows("index -1 is invalid", IllegalArgumentException.class, () -> store.get(-1));
    assertThrows("index 4 is invalid", IllegalArgumentException.class, () -> store.get(4));

  }*/

  /*@Test 
  public void testRemove(){
    PasswordStore store = new PasswordStore();
    store.add(e3);
    store.add(e2);
    store.add(e1);

    store.remove(1);
    assertEquals("size must be 2 after removing one entry", 2, store.getSize());
    assertSame("first entry must still be e1", e1, store.getFirstEntry());
    assertSame("e1 must reference e3 as next entry after e2 is removed", e3, e1.getNextEntry());

    store = new PasswordStore();
    store.add(e3);
    store.add(e2);
    store.add(e1);

    store.remove(0);
    assertEquals("size must be 2 after removing one entry", 2, store.getSize());
    assertSame("first entry must be e2 after removing e1", e2, store.getFirstEntry());

    store = new PasswordStore();
    store.add(e3);
    store.add(e2);
    store.add(e1);

    store.remove(2);
    assertEquals("size must be 2 after removing one entry", 2, store.getSize());
    assertSame("first entry must still be e1", e1, store.getFirstEntry());
    assertNull("e2 must point to null as next entry after removing e3", e2.getNextEntry());

    store.remove(0);
    store.remove(0);
    assertEquals("size must be 0 after removing all elements", 0, store.getSize());
    assertNull("first element must be zero after removing all elements", store.getFirstEntry());

    final PasswordStore finalStore = new PasswordStore();
    store.add(e3);
    store.add(e2);
    store.add(e1);
    assertThrows("index -1 is invalid", IllegalArgumentException.class, () -> finalStore.remove(-1));
    assertThrows("index 4 is invalid", IllegalArgumentException.class, () -> finalStore.remove(4));

  }*/


}

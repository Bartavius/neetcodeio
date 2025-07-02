import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import static org.junit.jupiter.api.Assertions.*;

public class ExampleTest {
    
    @BeforeEach
    void setUp() {
        // Setup code here
    }
    
    @Test
    void testAddition() {
        assertEquals(4, 2 + 2);
    }
    
    @Test
    void testString() {
        String expected = "Hello";
        String actual = "Hello";
        assertEquals(expected, actual);
    }
}
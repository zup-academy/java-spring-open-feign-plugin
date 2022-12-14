### Operations

- Creating a Feign HTTP Client

    1. Create a java interface
    2. Annotate the class level with `@FeignClient`, and define the name and url argument.
    3. Create a method signature, defining the return of your API and what are the arguments (Body and Params)
    4. annotate the method with one of the annotations referring to the HTTP verb mapping from the `org.springframework.web.bind.annotation` package;

        ```java
        @FeignClient(name = "bookClient", url = "https://books.com/api")
        public interface BookClient {
            @GetMapping("/{id}")
            ResponseEntity<Map<String,Object>> getBookById(@PathVariable Long id);
        }
        ```

    For more information read the [official documentation](https://docs.spring.io/spring-cloud-openfeign/docs/current/reference/html/#spring-cloud-feign)

- Testing an HTTP Client
    1. Create a test class and annotate it with `@SpringBootTest` and `@AutoConfigureWireMock`
    2. Inject your HTTP client dependency via attribute injection.
    3. Create a test method and annotate it with `@Test`
    4. Configure your Stub:
        1. Call the Wiremock API through the WireMock.StubFor() Object;
        2. Define which method will be served;
        3. Define an object to reply;
        4. Set the Body, Headers and HTTP Status of your Response.
        ```java
        @SpringBootTest
        @AutoConfigureWireMock
        class BookClientTest {
            @Autowired
            private ObjectMapper mapper;
            @Autowired
            private BookClient client;
            
            @Test
            @DisplayName("must return the book by id")
            void t1() throws JsonProcessingException {
                UUID bookId = UUID.randomUUID();
                BookResponse bookResponse = new BookResponse(bookId, "Domain Drive Design", "DDD", BigDecimal.TEN);
                String payload = mapper.writeValueAsString(bookResponse);
                String url = format("/api/books/%s", bookId);

                stubFor(
                        get(
                                urlEqualTo(url)
                        ).willReturn(
                                aResponse()
                                        .withStatus(200)
                                        .withHeader("Content-Type", "application/json")
                                        .withBody(payload)
                        )
                );

                ResponseEntity<BookResponse> response = client.getById(bookId);
                assertEquals(HttpStatus.OK, response.getStatusCode());
                assertEquals(MediaType.APPLICATION_JSON, response.getHeaders().getContentType());
                assertEquals(bookResponse, response.getBody());

            }
        ```
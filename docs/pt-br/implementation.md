### Operações

- Criando um Client HTTP Feign

    1. Crie uma interface java 
    2. Anote a nivel de classe com `@FeignClient`, e defina o argumento name e url.
    3. Crie uma assinatura de metodo, definindo o retorno da sua API  e quais são os argumentos (Body and Params)
    4. anote o metodo com uma das anotações referente ao mapeamento de verbo HTTP do package `org.springframework.web.bind.annotation`;

        ```java
        @FeignClient(name = "bookClient", url = "https://books.com/api")
        public interface BookClient {
            @GetMapping("/{id}")
            ResponseEntity<Map<String,Object>> getBookById(@PathVariable Long id); 
        }
        ```

    Para mais informações leia a [documentação oficial](https://docs.spring.io/spring-cloud-openfeign/docs/current/reference/html/#spring-cloud-feign)

- Testando um Client HTTP
    1. Crie uma classe de teste e anote com `@SpringBootTest` e `@AutoConfigureWireMock`
    2. Injete a depêndencia do seu client HTTP através da injeção via atributo.
    3. Crie um metodo de teste e anote-o com `@Test`
    4. Cofigure seu Stub:
        1. Chame a API do Wiremock através do Objeto WireMock.StubFor();
        2. Defina qual method será atendido;
        3. Defina um objeto para resposta;
        4. Defina o Body, Headers e Status HTTP da sua Response.  
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
 
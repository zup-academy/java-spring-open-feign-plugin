## Java Spring Open Feign Plugin

The **java-spring-open-feign-plugin** is a plugin to enable the ability to build HTTP Clients declaratively.

By applying this plugin to the Spring Boot project, you will get the following benefits:

1. Enable the use of Declarative Feign Clients in your Project.
2. Enable the creation of Declarative Feign Clients
3. Enable the ability to create MocksServers with Wiremock
3. All clients are configured with connect and read timeouts of 30sec , (with the possibility of modification)
4. Logging for HTTP calls from HTTP Clients
5. Generate production sample code and tests so you have a starting point for writing good integration tests with Sprint Boot and Test.

## How to use

It is necessary that [STK CLI](https://docs.stackspot.com/v4.1.0/docs/user-guide/user-quickstart/) be installed on your machine.

The following steps show how to apply the plugin to an existing Java Spring Boot application.

1. First, import our stack if you haven't already:
    ```sh
    stk import stack https://github.com/zup-academy/java-springboot-restapi-stack
    ```

2. Now, in the project directory, apply the plugin and answer all the questions:

    ```sh
    stk apply plugin java-springboot-restapi-stack/java-spring-open-feign-plugin
    ```

3. If your Main class (Annotated with `@SpringBootApplication`) is not in the Spring Initialize standard, set the path for the plugin configuration.

    inform in the following pattern: src.main.java.packages.YourApplicationClass

4. Still inside the project directory, you can check if the plugin was applied or not, checking the updated and created files:

    ```sh
    git status
    ```
Nice! You're ready for production I think 🥳

## support

If you need help, open a [Plugin Github repo issue](https://github.com/zup-academy/java-spring-open-feign-plugin).
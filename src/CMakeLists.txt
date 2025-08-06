add_library(comm STATIC
        comm/CommunicationManager.cpp
)
target_include_directories(comm PUBLIC ${CMAKE_SOURCE_DIR}/include/comm)

add_library(sensor_service STATIC
        sensor_service/SensorService.cpp
)
target_include_directories(sensor_service PUBLIC ${CMAKE_SOURCE_DIR}/include/sensor_service)
target_link_libraries(sensor_service comm)

add_library(client_app STATIC
        client_app/ClientApp.cpp
)
target_include_directories(client_app PUBLIC ${CMAKE_SOURCE_DIR}/include/client_app)
target_link_libraries(client_app comm)

add_library(logger STATIC
        utils/Logger.cpp
)
target_include_directories(logger PUBLIC ${CMAKE_SOURCE_DIR}/include/utils)

add_library(config_manager STATIC
        utils/ConfigManager.cpp
)
target_include_directories(config_manager PUBLIC ${CMAKE_SOURCE_DIR}/include/utils)

add_library(crypto_manager STATIC
        crypto/CryptoManager.cpp
)
target_include_directories(crypto_manager PUBLIC ${CMAKE_SOURCE_DIR}/include/crypto)

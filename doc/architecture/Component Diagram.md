# System Architecture Overview

The following UML-style component diagram illustrates the high-level architecture

    +-------------------------------------------------------------+
    |                       Application Layer                     |
    |                                                             |
    |  +------------------+         +-------------------------+   |
    |  |  ClientApp       |<------->|    CommunicationManager |   |
    |  |------------------|         +-------------------------+   |
    |  | - RequestSensor()|                                       |
    |  | - HandleData()   |                                       |
    |  +------------------+                                       |
    |                                                             |
    |  +------------------+         +-------------------------+   |
    |  |  SensorService   |<------->|    CommunicationManager |   |
    |  |------------------|         +-------------------------+   |
    |  | - GenerateData() |                                       |
    |  | - SendData()     |                                       |
    |  +------------------+                                       |
    |                                                             |
    +-------------------------------------------------------------+
                    ↑                         ↑
                    |                         |
        +------------------+    +----------------------+
        |    Logger        |    |    ConfigManager     |
        +------------------+    +----------------------+
        | - LogInfo()      |    | - LoadManifest()     |
        | - LogError()     |    | - ProvideServiceInfo |
        +------------------+    +----------------------+

                               ↑
                               |
                     +-------------------+
                     |  CryptoManager    |
                     +-------------------+
                     | - EncryptData()   |
                     | - SecureChannel() |
                     +-------------------+

- **ClientApp**: Initiates service requests. Discovers *SensorsService* via *ConfigManager*, connects via *CommunicationManager*.
- **SensorService**: Processes and returns the requested data. Generates data every 1-5 seconds or 10-100ms and sends via *CommunicationManager*
- **Logger**: Records runtime information and error logs.
- **ConfigManager**: Loads configuration from YAML/JSON manifests.
- **CryptoManager**: Ensures data security and transport integrity. Secures the channel (ex: TLS).
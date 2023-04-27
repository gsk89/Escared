#######################################################################################
#                                                                                     #
#    Para poder utilizar el siguiente script es necesario contar con lo siguiente:    #
#                                                                                     #
#        1.- Configurar el servidor de SSH en el equipo de telecomunicaciones.        #
#            Ejemplo en cisco:                                                        #
#        
#            Router$ enable
#            Router# configure terminal
#            Router(config)# hostname Oficina
#            Oficina(config)# ip domain-name Oficina.local
#            Oficina(config)# crypto key generate rsa
#            Oficina(config)# ip ssh version 2
#            Oficina(config)# ip ssh authentication-retries 3
#            Oficina(config)# ip ssh time-out 30
#            Oficina(config)# line vty 0 1
#            Oficina(config-line)# tra

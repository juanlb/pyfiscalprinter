# Creado siguiendo ejemplo en http://essiene.blogspot.com/2005/04/python-windows-services.html
# Seguir los pasos de ese post para hacerlo funcionar

import win32service
import win32serviceutil

class EpsonFiscalDriverService(win32serviceutil.ServiceFramework):
    _svc_name_ = "genericFiscalDriver"
    _svc_display_name_ = "Servidor de Impresora Fiscal"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)

    def SvcDoRun(self):
        import servicemanager

	from genericFiscalDriver import socketServer

        servicemanager.LogInfoMsg("genericFiscalDriver - Iniciando Servidor")
	self.server = socketServer("Hasar", "", 12345, "COM1", 9600, 60, True)
        servicemanager.LogInfoMsg("genericFiscalDriver - Servidor Construido, sirviendo eternamente")
	self.server.serve_forever()

    def SvcStop(self):
        import servicemanager

        servicemanager.LogInfoMsg("genericFiscalDriver - Deteniendo el servicio")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
	self.server.shutdown()

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(EpsonFiscalDriverService)


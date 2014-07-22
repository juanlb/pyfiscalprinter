# -*- coding: iso-8859-1 -*-

import sys

# Crear el controlador para la impresora fiscal:
if False or '--epson' in sys.argv:
    from epsonPrinter import EpsonPrinter
    print "Usando driver de Epson"
    model = ["tickeadoras", "epsonlx300+", "tm-220-af"][1]
    printer = EpsonPrinter(deviceFile="COM2", model=model, dummy=False)
else:
    from hasarPrinter import HasarPrinter
    print "Usando driver de Hasar"
    model = ["615", "715v1", "715v2", "320"][0]
    printer = HasarPrinter(deviceFile="/dev/ttyUSB0", model=320, dummy=False)

# Obtener el último número de factura emitida
#number = printer.getPrinterId() #+ 1
if False:
    number = printer.getLastNumber("B") + 1
    print "datos ", number
    #print printer.cancelAnyDocument()
    #print printer.getErrors()
    print printer.getPrinterId()

# Abrir un comprobante fiscal:
#if model in ("epsonlx300+", ):
#    # TODO: ajustar en openTicket
#    printer.openBillTicket("B", "Nombre y Apellido", "Direccion", "0", # nro_doc
#                           printer.DOC_TYPE_SIN_CALIFICADOR, 
#                           printer.IVA_TYPE_CONSUMIDOR_FINAL)
#else:
#    printer.openTicket()

#print printer.getWarnings('A')

if False:
    #Cancelar
    print printer.cancelAnyDocument()
    #print printer.getErrors()
    #print printer.getSubtotal()
else:
    printer.openBillTicket("B", "Nombre y Apellido", "Direccion", "0", # nro_doc
                               printer.DOC_TYPE_SIN_CALIFICADOR, 
                               printer.IVA_TYPE_CONSUMIDOR_FINAL)

    #printer.openTicket()

    #printer.printNonFiscalText("Si anda me emplumo")
    #printer.setHeader(["Test de Header"])

    # Facturar Caramelos a $ 1,50, con 21% de IVA, 2 paquetes de cigarrillos a $ 10
    printer.addItem("CIGARRILLOS", 2, 1.0, 21.0,  discount=0, discountDescription="")
    #printer.addItem("CARAMELOS", 1, 1.50, 21.0, discount=0, discountDescription="")
    printer.addItem("CARAMELOS", 1, 'asdf', 21.0, discount=0, discountDescription="")
    #print printer.getSubtotal()
    

    # Pago en efectivo. Si el importe fuera mayor la impresora va a
    # calcular el vuelto
    # printer.addPayment("Efectivo", 11.50)

    # Cerrar el comprobante fiscal
    # printer.closeDocument()


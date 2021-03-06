import json

def set_login_params(SID):
	params = {'hdnServer':'.77',
		'hdnSID':SID,
		'hdnLangCode':'en-US',
		'hdnPOS':'US',
		'hdnClient':'66.91.220.35',
		'hdnInactive':'false',
		'hdnAccountNumber':'',
		'hdnAccountNumberE':'',
		'hdnAccountStatus':'',
		'__EVENTTARGET':'',
		'__EVENTARGUMENT':'',
		'hdnTiming':'0.921639 seconds',
		'__LASTFOCUS':'',
		'__VIEWSTATE=/wEPDwUKMTk1MTA4NjkxNQ9kFgJmD2QWAgIDDxYCHghvbnVubG9hZAUSUHVyY2hhc2VBYmFuZG9uKCk7FgICAQ8WAh4GYWN0aW9uBS1odHRwczovL3d3dy51bml0ZWQuY29tL3dlYi9lbi1VUy9kZWZhdWx0LmFzcHgWBAIFD2QWAgIJD2QWAgIDD2QWCgIBDxYCHglpbm5lcmh0bWxlZAIFDxYCHwIFlwM8YSBocmVmPSJodHRwOi8vY3J1aXNlcy51bml0ZWQuY29tLz9jbV9tbWM9TGluay1fLVVBTC1TaXRlX1JlZmVycmFsLV8tMjAxMjExMTktR2VuLUVuZy1GbHQtXy1HZW5lcmljX0hQJmludF9zb3VyY2U9dWFtZXImaW50X21lZGl1bT11YWNvbSZpbnRfY2FtcGFpZ249dW5pdGVkX2NydWlzZXMmaW50X2NvbnRlbnQ9ZW5nbGlzaCZwYXJ0bmVyX2NhdGVnb3J5PWFuY2lsbGFyeSZwYXJ0bmVyX25hbWU9dWNfd3RoX2ZsaWdodCZhc3NldF9wb3NpdGlvbj1obGMxJnRhcmdldGluZz11c19hbGwmbGF1bmNoX2RhdGU9MjAxMi0xMS0xOSI PGltZyBzcmM9Ii93ZWIvZW4tVVMvaW1nL2hvbWVwYWdlL2NydWlzZTIwMDkwOC5naWYiIGFsdD0iQm9vayBVbml0ZWQgQ3J1aXNlcyIgaGVpZ2h0PSIzNSIgd2lkdGg9IjMwMCI PC9hPmQCBw8WAh8CBZQLPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPg0KPCEtLQ0KDQppZiAoImh0dHBzOiIgPT0gZG9jdW1lbnQubG9jYXRpb24ucHJvdG9jb2wpIHsNCiAgICBPQVNfdXJsID0gJ2h0dHBzOi8vb2FzYzE3LjI0N3JlYWxtZWRpYS5jb20nOw0KICAgIE9BU19zaXRlcGFnZSA9ICd3d3cudW5pdGVkLmNvbS9ob21lcGFnZSc7DQogICAgT0FTX3BvcyA9ICdCb3R0b21MZWZ0LEJvdHRvbVJpZ2h0IUJvdHRvbUxlZnQnOw0KICAgIE9BU19xdWVyeSA9ICcnOw0KDQogICAgaWYgKHR5cGVvZiBPQVNfUk5TID09ICd1bmRlZmluZWQnKXsNCiAgICAgICAgdmFyIE9BU19STiA9IG5ldyBTdHJpbmcgKE1hdGgucmFuZG9tKCkpOw0KICAgICAgICB2YXIgT0FTX1JOUyA9IE9BU19STi5zdWJzdHJpbmcoMiwgMTEpOw0KfQ0KICAgIC8qIEJlZ2luIE9BU19Cb3R0b21MZWZ0ICovZG9jdW1lbnQud3JpdGUoJzxzY3InICsgJ2lwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiIHNyYz0iJyArIE9BU191cmwgKyAnL1JlYWxNZWRpYS9hZHMvYWRzdHJlYW1fanguYWRzLycgKyBPQVNfc2l0ZXBhZ2UgKyAnLzEnICsgT0FTX1JOUyArICdAJyArIE9BU19wb3MgKyAnPycgKyBPQVNfcXVlcnkgKyAnIj48L3NjcicgKyAnaXB0PicpOy8qIEVuZCBPQVNfQm90dG9tTGVmdCAqLw0KfSBlbHNlIHsgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgDQogICAgT0FTX3VybCA9ICdodHRwOi8vb2FzYzE3LjI0N3JlYWxtZWRpYS5jb20nOw0KICAgIE9BU19zaXRlcGFnZSA9ICd3d3cudW5pdGVkLmNvbS9ob21lcGFnZSc7DQogICAgT0FTX3BvcyA9ICdCb3R0b21MZWZ0LEJvdHRvbVJpZ2h0IUJvdHRvbUxlZnQnOw0KICAgIE9BU19xdWVyeSA9ICcnOw0KDQogICAgaWYgKHR5cGVvZiBPQVNfUk5TID09ICd1bmRlZmluZWQnKXsNCiAgICAgICAgdmFyIE9BU19STiA9IG5ldyBTdHJpbmcgKE1hdGgucmFuZG9tKCkpOw0KICAgICAgICB2YXIgT0FTX1JOUyA9IE9BU19STi5zdWJzdHJpbmcoMiwgMTEpOw0KfQ0KICAgIGRvY3VtZW50LndyaXRlKCc8c2NyJyArICdpcHQgdHlwZT0idGV4dC9qYXZhc2NyaXB0IiBzcmM9IicgKyBPQVNfdXJsICsgJy9SZWFsTWVkaWEvYWRzL2Fkc3RyZWFtX2p4LmFkcy8nICsgT0FTX3NpdGVwYWdlICsgJy8xJyArIE9BU19STlMgKyAnQCcgKyBPQVNfcG9zICsgJz8nICsgT0FTX3F1ZXJ5ICsgJyI PC9zY3InICsgJ2lwdD4nKTsNCn0NCi8vIC0tPg0KPC9zY3JpcHQ ZAIJDxYCHgRUZXh0BYQGc3RyQmFubmVyU3JjQXR0cmlidXRlcz0lMmZ3ZWIlMmZlbi1VUyUyZmNvbnRlbnQlMmZoYmFuMiUyZjIwMTIwNzAzX05ld1dpbmRvd0Jvb2wuc3dmJTNmYmclM2QlMmZ3ZWIlMmZlbi11cyUyZmltZyUyZnRndCUyZmhiYW4yJTJmMjAxMzExMTFfSGFpeWFucmVsaWVmLmpwZyUyNmhlYWRMaW5lJTNkJTI2c3ViSGVhZCUzZCUyNnN0ckNUQSUzZCUyNmJOZXdXaW5kb3clM2R0cnVlJTI2c3RyQmFzZVVSTCUzZGh0dHAlMjUzQSUyNTJGJTI1MkZ3d3cuY3Jvd2RyaXNlLmNvbSUyNTJGdW5pdGVkcmVsaWVmJTI1M0ZpbnRfc291cmNlJTI1M0RjY2ElMjUyNmludF9tZWRpdW0lMjUzRHVhY29tJTI1MjZpbnRfY2FtcGFpZ24lMjUzRGhhaXlhbl9yZWxpZWZfYWxtMTI3MjYlMjUyNmludF9jb250ZW50JTI1M0R1YS5yZWxpZWYlMjUyNnBhcnRuZXJfbmFtZSUyNTNEbXAlMjUyNmFzc2V0X3Bvc2l0aW9uJTI1M0RIQkFOMiUyNTI2bGF1bmNoX2RhdGUlMjUzRDIwMTMtMTEtMTEmc3RyQmFubmVySHJlZkF0dHJpYnV0ZXM9aHR0cCUyNTNBJTI1MkYlMjUyRnd3dy5jcm93ZHJpc2UuY29tJTI1MkZ1bml0ZWRyZWxpZWYlMjUzRmludF9zb3VyY2UlMjUzRGNjYSUyNTI2aW50X21lZGl1bSUyNTNEdWFjb20lMjUyNmludF9jYW1wYWlnbiUyNTNEaGFpeWFuX3JlbGllZl9hbG0xMjcyNiUyNTI2aW50X2NvbnRlbnQlMjUzRHVhLnJlbGllZiUyNTI2cGFydG5lcl9uYW1lJTI1M0RtcCUyNTI2YXNzZXRfcG9zaXRpb24lMjUzREhCQU4yJTI1MjZsYXVuY2hfZGF0ZSUyNTNEMjAxMy0xMS0xMWQCDw9kFgYCAQ8PFgIeC05hdmlnYXRlVXJsBSkvdHJhdmVsL2NoZWNraW4vc3RhcnQuYXNweD9MYW5nQ29kZT1lbi1VU2RkAgUPZBYEAgMPDxYCHg1PbkNsaWVudENsaWNrBW1kb2N1bWVudC5mb3Jtc1swXS5hY3Rpb249J2h0dHA6Ly93d3cudW5pdGVkLmNvbS93ZWIvZW4tVVMvZGVmYXVsdC5hc3B4P1NJRD0zNDNGRkI5MTA1MTA0QjAyODFCQTU3QjlERTM4RDQwNSc7ZGQCBQ8PFgIfBAUpL3RyYXZlbC9jaGVja2luL3N0YXJ0LmFzcHg/TGFuZ0NvZGU9ZW4tVVNkZAIHD2QWCgIBDxYCHgdWaXNpYmxlZxYCZg8PFgIfBmhkFgICBg8QZA8WAWYWARAFBlVuaXRlZAUCVUFnFgFmZAIFDxBkDxYEZgIBAgICAxYEDwUNV2VkLiwgTm92LiAxMwUKMTEvMTMvMjAxMw8FDVRodS4sIE5vdi4gMTQFCjExLzE0LzIwMTMPBQ1GcmkuLCBOb3YuIDE1BQoxMS8xNS8yMDEzDwUNU2F0LiwgTm92LiAxNgUKMTEvMTYvMjAxM2RkAgcPZBYIAggPZBYCAgEPFgIfAgWUAUNpdHkgb3IgPGEgaHJlZj0iamF2YXNjcmlwdDpPcGVuQWlycG9ydHModGhpcywnY3RsMDBfQ29udGVudEluZm9fQ2hlY2tpbmZsaWdodHN0YXR1c19PcmlnaW5fdHh0T3JpZ2luJywnT3JpZ2luQWlycG9ydCcpOyIgdGFiaW5kZXg9Ii0xIj5haXJwb3J0PC9hPjpkAgwPZBYCAgIPFgweDUVuYWJsZUNhY2hpbmdnHg1Vc2VDb250ZXh0S2V5Zx4SQ29tcGxldGlvblNldENvdW50AtwLHhJDb21wbGV0aW9uSW50ZXJ2YWwC gEeCkNvbnRleHRLZXkFBWVuLVVTHgdFbmFibGVkZ2QCDg8QDxYCHgtfIURhdGFCb3VuZGcWAh4Ib25jaGFuZ2UFZWphdmFzY3JpcHQ6ZG9jdW1lbnQuZm9ybXNbMF0uY3RsMDBfQ29udGVudEluZm9fQ2hlY2tpbmZsaWdodHN0YXR1c19PcmlnaW5fdHh0T3JpZ2luLnZhbHVlPXRoaXMudmFsdWU7ZBYAZAIQDxYEHg1XYXRlcm1hcmtUZXh0BQRGcm9tHwxnZAIJD2QWCgIHD2QWAgIBDxYCHwIFowFDaXR5IG9yIDxhIGhyZWY9ImphdmFzY3JpcHQ6T3BlbkFpcnBvcnRzKHRoaXMsJ2N0bDAwX0NvbnRlbnRJbmZvX0NoZWNraW5mbGlnaHRzdGF0dXNfRGVzdGluYXRpb25fdHh0RGVzdGluYXRpb24nLCdEZXN0aW5hdGlvbkFpcnBvcnQnKTsiIHRhYmluZGV4PSItMSI YWlycG9ydDwvYT46ZAIJDxAPFgIfDWdkZBYAZAIND2QWAgICDxYMHwdnHwhnHwkC3AsfCgL6AR8LBQVlbi1VUx8MZ2QCDw8QDxYCHw1nFgIfDgVvamF2YXNjcmlwdDpkb2N1bWVudC5mb3Jtc1swXS5jdGwwMF9Db250ZW50SW5mb19DaGVja2luZmxpZ2h0c3RhdHVzX0Rlc3RpbmF0aW9uX3R4dERlc3RpbmF0aW9uLnZhbHVlPXRoaXMudmFsdWU7ZBYAZAIRDxYEHw8FAlRvHwxnZAILDw8WAh8FBUhkb2N1bWVudC5mb3Jtc1swXS5hY3Rpb249J2h0dHA6Ly93d3cudW5pdGVkLmNvbS93ZWIvZW4tVVMvZGVmYXVsdC5hc3B4JztkZAILDw8WAh8GaGRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYWBRhjdGwwMCRDdXN0b21lckhlYWRlciRyZDEFGGN0bDAwJEN1c3RvbWVySGVhZGVyJHJkMgUYY3RsMDAkQ3VzdG9tZXJIZWFkZXIkcmQzBRxjdGwwMCRDdXN0b21lckhlYWRlciRjaGtTYXZlBSljdGwwMCRDb250ZW50SW5mbyRCb29raW5nMSRyZG9TZWFyY2hUeXBlMQUpY3RsMDAkQ29udGVudEluZm8kQm9va2luZzEkcmRvU2VhcmNoVHlwZTIFKWN0bDAwJENvbnRlbnRJbmZvJEJvb2tpbmcxJHJkb1NlYXJjaFR5cGUyBS5jdGwwMCRDb250ZW50SW5mbyRCb29raW5nMSROZWFyYnlhaXIkY2hrRmx0T3B0BSxjdGwwMCRDb250ZW50SW5mbyRCb29raW5nMSRBbHREYXRlJGNoa0ZsdE9wdAU2Y3RsMDAkQ29udGVudEluZm8kQm9va2luZzEkRGVwRGF0ZVRpbWUkcmRvRGF0ZVNwZWNpZmljBTJjdGwwMCRDb250ZW50SW5mbyRCb29raW5nMSREZXBEYXRlVGltZSRyZG9EYXRlRmxleAUyY3RsMDAkQ29udGVudEluZm8kQm9va2luZzEkRGVwRGF0ZVRpbWUkcmRvRGF0ZUZsZXgFMGN0bDAwJENvbnRlbnRJbmZvJEJvb2tpbmcxJFNlYXJjaEJ5JHJkb3NlYXJjaGJ5MQUwY3RsMDAkQ29udGVudEluZm8kQm9va2luZzEkU2VhcmNoQnkkcmRvc2VhcmNoYnkyBTBjdGwwMCRDb250ZW50SW5mbyRCb29raW5nMSRTZWFyY2hCeSRyZG9zZWFyY2hieTIFMGN0bDAwJENvbnRlbnRJbmZvJEJvb2tpbmcxJFNlYXJjaEJ5JHJkb3NlYXJjaGJ5MwUwY3RsMDAkQ29udGVudEluZm8kQm9va2luZzEkU2VhcmNoQnkkcmRvc2VhcmNoYnkzBStjdGwwMCRDb250ZW50SW5mbyRCb29raW5nMSREaXJlY3QkY2hrRmx0T3B0BSVjdGwwMCRDb250ZW50SW5mbyRtYW5hZ2VyZXMkcmRvRmxpZ2h0BSJjdGwwMCRDb250ZW50SW5mbyRtYW5hZ2VyZXMkcmRvQ2FyBSJjdGwwMCRDb250ZW50SW5mbyRtYW5hZ2VyZXMkcmRvQ2FyBTRjdGwwMCRDb250ZW50SW5mbyRhY2NvdW50c3VtbWFyeSRyZW1lbWJlcm1lJGNoa1JlbU1lnl2VshW SenmBpabWRL1uiA1s14':'',
		'ctl00$CustomerHeader$ddlCountries':'US',
		'ctl00$CustomerHeader$rdlang':'en-us',
		'ctl00$CustomerHeader$chkSave':'on',
		'ctl00$CustomerHeader$countryText':'',
		'ctl00$CustomerHeader$langText':'',
		'ctl00$ContentInfo$Booking1$hdnText':'Award Travel',
		'ctl00$ContentInfo$Booking1$SearchType':'rdoSearchType1',
		'ctl00$ContentInfo$Booking1$Origin$txtOrigin':'Frankfurt, Germany (FRA)',
		'ctl00$ContentInfo$Booking1$Origin$TBWE01_ClientState':'',
		'ctl00$ContentInfo$Booking1$Destination$txtDestination':'Washington, DC (IAD - Dulles)',
		'ctl00$ContentInfo$Booking1$Destination$TBWE01_ClientState':'',
		'ctl00$ContentInfo$Booking1$DepDateTime$DateFlex':'rdoDateSpecific',
		'ctl00$ContentInfo$Booking1$DepDateTime$Depdate$txtDptDate':'mm/dd/yyyy',
		'ctl00$ContentInfo$Booking1$DepDateTime$Deptime$cboDptTime':' ',
		'ctl00$ContentInfo$Booking1$DepDateTime$MonthList1$cboMonth':'12/1/2013',
		'ctl00$ContentInfo$Booking1$DepDateTime$LengthOfStay$cboLengthOfStay':'6',
		'ctl00$ContentInfo$Booking1$RetDateTime$Retdate$txtRetDate':'mm/dd/yyyy',
		'ctl00$ContentInfo$Booking1$RetDateTime$Rettime$cboDptTime':' ',
		'ctl00$ContentInfo$Booking1$Adult$cboAdult':'1',
		'ctl00$ContentInfo$Booking1$Offercode$txtPromoCode':'',
		'ctl00$ContentInfo$Booking1$Cabins$cboCabin':'Coach',
		'ctl00$ContentInfo$Booking1$SearchBy$SearchBy':'rdosearchby1',
		'ctl00$ContentInfo$Booking1$Pckuploc$txtOrigin':'',
		'ctl00$ContentInfo$Booking1$Returnlocdropoff$txtDestination':'Same as pick-up',
		'ctl00$ContentInfo$Booking1$Pickupdate$txtDptDate':'mm/dd/yyyy',
		'ctl00$ContentInfo$Booking1$Pickuptime$cboPickUpTime':'10:00AM',
		'ctl00$ContentInfo$Booking1$Dropoffdate$txtRetDate':'mm/dd/yyyy',
		'ctl00$ContentInfo$Booking1$Dropofftime$cboRetTime':'10:00AM',
		'ctl00$ContentInfo$Booking1$Cartype$cboCarType':'5',
		'ctl00$ContentInfo$Checkinflightstatus$Onepassconfirm$txtOPNum':'',
		'ctl00$ContentInfo$Checkinflightstatus$FlightNumber$txtFltNum':'',
		'ctl00$ContentInfo$Checkinflightstatus$cboFltDates':'12/14/2013',
		'ctl00$ContentInfo$Checkinflightstatus$Origin$txtOrigin':'',
		'ctl00$ContentInfo$Checkinflightstatus$Origin$TBWE01_ClientState':'',
		'ctl00$ContentInfo$Checkinflightstatus$Destination$txtDestination':'',
		'ctl00$ContentInfo$Checkinflightstatus$Destination$TBWE01_ClientState':'',
		'ctl00$ContentInfo$manageres$confirmationOptions':'rdoFlight',
		'ctl00$ContentInfo$manageres$ConfNum$txtPNR':'',
		'ctl00$ContentInfo$manageres$LastName$txtLName':'',
		'ctl00$ContentInfo$accountsummary$btnOnePassSignIn':'Sign In',
		'hiddenInputToUpdateATBuffer_CommonToolkitScripts':'1'
	}
	return params


def set_search_params(SID):
	params = {'hdnServer':'.127',
	'hdnSID':SID,
	'hdnLangCode':'en-US',
	'hdnPOS':'US',
	'hdnClient':'66.91.220.35',
	'hdnInactive':'false',
	'hdnAccountNumber':'NP904725',
	'hdnAccountNumberE':'/vTUgnzC9qgJlfdjZZRZMw==',
	'hdnAccountStatus':'0',
	'hdnTiming':'0.781125 seconds',
	'__EVENTTARGET':'',
	'__EVENTARGUMENT':'',
	'__LASTFOCUS':'',
	'__VIEWSTATE=/wEPDwUKMTk1MTA4NjkxNQ9kFgJmD2QWAgIDDxYCHghvbnVubG9hZAUSUHVyY2hhc2VBYmFuZG9uKCk7FgICAQ8WAh4GYWN0aW9uBS1odHRwczovL3d3dy51bml0ZWQuY29tL3dlYi9lbi1VUy9EZWZhdWx0LmFzcHgWBAIFD2QWAgIJD2QWAgIDD2QWCgIBDxYCHglpbm5lcmh0bWxlZAIFDxYCHwIFlwM8YSBocmVmPSJodHRwOi8vY3J1aXNlcy51bml0ZWQuY29tLz9jbV9tbWM9TGluay1fLVVBTC1TaXRlX1JlZmVycmFsLV8tMjAxMjExMTktR2VuLUVuZy1GbHQtXy1HZW5lcmljX0hQJmludF9zb3VyY2U9dWFtZXImaW50X21lZGl1bT11YWNvbSZpbnRfY2FtcGFpZ249dW5pdGVkX2NydWlzZXMmaW50X2NvbnRlbnQ9ZW5nbGlzaCZwYXJ0bmVyX2NhdGVnb3J5PWFuY2lsbGFyeSZwYXJ0bmVyX25hbWU9dWNfd3RoX2ZsaWdodCZhc3NldF9wb3NpdGlvbj1obGMxJnRhcmdldGluZz11c19hbGwmbGF1bmNoX2RhdGU9MjAxMi0xMS0xOSI\x2BPGltZyBzcmM9Ii93ZWIvZW4tVVMvaW1nL2hvbWVwYWdlL2NydWlzZTIwMDkwOC5naWYiIGFsdD0iQm9vayBVbml0ZWQgQ3J1aXNlcyIgaGVpZ2h0PSIzNSIgd2lkdGg9IjMwMCI\x2BPC9hPmQCBw8WAh8CBZQLPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPg0KPCEtLQ0KDQppZiAoImh0dHBzOiIgPT0gZG9jdW1lbnQubG9jYXRpb24ucHJvdG9jb2wpIHsNCiAgICBPQVNfdXJsID0gJ2h0dHBzOi8vb2FzYzE3LjI0N3JlYWxtZWRpYS5jb20nOw0KICAgIE9BU19zaXRlcGFnZSA9ICd3d3cudW5pdGVkLmNvbS9ob21lcGFnZSc7DQogICAgT0FTX3BvcyA9ICdCb3R0b21MZWZ0LEJvdHRvbVJpZ2h0IUJvdHRvbUxlZnQnOw0KICAgIE9BU19xdWVyeSA9ICcnOw0KDQogICAgaWYgKHR5cGVvZiBPQVNfUk5TID09ICd1bmRlZmluZWQnKXsNCiAgICAgICAgdmFyIE9BU19STiA9IG5ldyBTdHJpbmcgKE1hdGgucmFuZG9tKCkpOw0KICAgICAgICB2YXIgT0FTX1JOUyA9IE9BU19STi5zdWJzdHJpbmcoMiwgMTEpOw0KfQ0KICAgIC8qIEJlZ2luIE9BU19Cb3R0b21MZWZ0ICovZG9jdW1lbnQud3JpdGUoJzxzY3InICsgJ2lwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiIHNyYz0iJyArIE9BU191cmwgKyAnL1JlYWxNZWRpYS9hZHMvYWRzdHJlYW1fanguYWRzLycgKyBPQVNfc2l0ZXBhZ2UgKyAnLzEnICsgT0FTX1JOUyArICdAJyArIE9BU19wb3MgKyAnPycgKyBPQVNfcXVlcnkgKyAnIj48L3NjcicgKyAnaXB0PicpOy8qIEVuZCBPQVNfQm90dG9tTGVmdCAqLw0KfSBlbHNlIHsgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgDQogICAgT0FTX3VybCA9ICdodHRwOi8vb2FzYzE3LjI0N3JlYWxtZWRpYS5jb20nOw0KICAgIE9BU19zaXRlcGFnZSA9ICd3d3cudW5pdGVkLmNvbS9ob21lcGFnZSc7DQogICAgT0FTX3BvcyA9ICdCb3R0b21MZWZ0LEJvdHRvbVJpZ2h0IUJvdHRvbUxlZnQnOw0KICAgIE9BU19xdWVyeSA9ICcnOw0KDQogICAgaWYgKHR5cGVvZiBPQVNfUk5TID09ICd1bmRlZmluZWQnKXsNCiAgICAgICAgdmFyIE9BU19STiA9IG5ldyBTdHJpbmcgKE1hdGgucmFuZG9tKCkpOw0KICAgICAgICB2YXIgT0FTX1JOUyA9IE9BU19STi5zdWJzdHJpbmcoMiwgMTEpOw0KfQ0KICAgIGRvY3VtZW50LndyaXRlKCc8c2NyJyArICdpcHQgdHlwZT0idGV4dC9qYXZhc2NyaXB0IiBzcmM9IicgKyBPQVNfdXJsICsgJy9SZWFsTWVkaWEvYWRzL2Fkc3RyZWFtX2p4LmFkcy8nICsgT0FTX3NpdGVwYWdlICsgJy8xJyArIE9BU19STlMgKyAnQCcgKyBPQVNfcG9zICsgJz8nICsgT0FTX3F1ZXJ5ICsgJyI\x2BPC9zY3InICsgJ2lwdD4nKTsNCn0NCi8vIC0tPg0KPC9zY3JpcHQ\x2BZAIJDxYCHgRUZXh0BYQGc3RyQmFubmVyU3JjQXR0cmlidXRlcz0lMmZ3ZWIlMmZlbi1VUyUyZmNvbnRlbnQlMmZoYmFuMiUyZjIwMTIwNzAzX05ld1dpbmRvd0Jvb2wuc3dmJTNmYmclM2QlMmZ3ZWIlMmZlbi11cyUyZmltZyUyZnRndCUyZmhiYW4yJTJmMjAxMzExMTFfSGFpeWFucmVsaWVmLmpwZyUyNmhlYWRMaW5lJTNkJTI2c3ViSGVhZCUzZCUyNnN0ckNUQSUzZCUyNmJOZXdXaW5kb3clM2R0cnVlJTI2c3RyQmFzZVVSTCUzZGh0dHAlMjUzQSUyNTJGJTI1MkZ3d3cuY3Jvd2RyaXNlLmNvbSUyNTJGdW5pdGVkcmVsaWVmJTI1M0ZpbnRfc291cmNlJTI1M0RjY2ElMjUyNmludF9tZWRpdW0lMjUzRHVhY29tJTI1MjZpbnRfY2FtcGFpZ24lMjUzRGhhaXlhbl9yZWxpZWZfYWxtMTI3MjYlMjUyNmludF9jb250ZW50JTI1M0R1YS5yZWxpZWYlMjUyNnBhcnRuZXJfbmFtZSUyNTNEbXAlMjUyNmFzc2V0X3Bvc2l0aW9uJTI1M0RIQkFOMiUyNTI2bGF1bmNoX2RhdGUlMjUzRDIwMTMtMTEtMTEmc3RyQmFubmVySHJlZkF0dHJpYnV0ZXM9aHR0cCUyNTNBJTI1MkYlMjUyRnd3dy5jcm93ZHJpc2UuY29tJTI1MkZ1bml0ZWRyZWxpZWYlMjUzRmludF9zb3VyY2UlMjUzRGNjYSUyNTI2aW50X21lZGl1bSUyNTNEdWFjb20lMjUyNmludF9jYW1wYWlnbiUyNTNEaGFpeWFuX3JlbGllZl9hbG0xMjcyNiUyNTI2aW50X2NvbnRlbnQlMjUzRHVhLnJlbGllZiUyNTI2cGFydG5lcl9uYW1lJTI1M0RtcCUyNTI2YXNzZXRfcG9zaXRpb24lMjUzREhCQU4yJTI1MjZsYXVuY2hfZGF0ZSUyNTNEMjAxMy0xMS0xMWQCDw9kFgYCAQ8PFgQeC05hdmlnYXRlVXJsBTgvdHJhdmVsL2NoZWNraW4vc3RhcnQuYXNweD9MYW5nQ29kZT1lbi1VUz9MYW5nQ29kZT1lbi1VUx8DBRNQcmludCBCb2FyZGluZyBQYXNzZGQCBQ9kFgQCAw8PFgIeDU9uQ2xpZW50Q2xpY2sFSGRvY3VtZW50LmZvcm1zWzBdLmFjdGlvbj0naHR0cDovL3d3dy51bml0ZWQuY29tL3dlYi9lbi1VUy9EZWZhdWx0LmFzcHgnO2RkAgUPDxYCHwQFOC90cmF2ZWwvY2hlY2tpbi9zdGFydC5hc3B4P0xhbmdDb2RlPWVuLVVTP0xhbmdDb2RlPWVuLVVTZGQCBw9kFgoCAQ8WAh4HVmlzaWJsZWcWAmYPDxYCHwZoZBYCAgYPEGQPFgFmFgEQBQZVbml0ZWQFAlVBZxYBZmQCBQ8QZA8WBGYCAQICAgMWBA8FDVRodS4sIE5vdi4gMTQFCjExLzE0LzIwMTMPBQ1GcmkuLCBOb3YuIDE1BQoxMS8xNS8yMDEzDwUNU2F0LiwgTm92LiAxNgUKMTEvMTYvMjAxMw8FDVN1bi4sIE5vdi4gMTcFCjExLzE3LzIwMTNkZAIHD2QWCAIID2QWAgIBDxYCHwIFlAFDaXR5IG9yIDxhIGhyZWY9ImphdmFzY3JpcHQ6T3BlbkFpcnBvcnRzKHRoaXMsJ2N0bDAwX0NvbnRlbnRJbmZvX0NoZWNraW5mbGlnaHRzdGF0dXNfT3JpZ2luX3R4dE9yaWdpbicsJ09yaWdpbkFpcnBvcnQnKTsiIHRhYmluZGV4PSItMSI\x2BYWlycG9ydDwvYT46ZAIMD2QWAgICDxYMHg1FbmFibGVDYWNoaW5nZx4NVXNlQ29udGV4dEtleWceEkNvbXBsZXRpb25TZXRDb3VudALcCx4SQ29tcGxldGlvbkludGVydmFsAvoBHgpDb250ZXh0S2V5BQVlbi1VUx4HRW5hYmxlZGdkAg4PEA8WAh4LXyFEYXRhQm91bmRnFgIeCG9uY2hhbmdlBWVqYXZhc2NyaXB0OmRvY3VtZW50LmZvcm1zWzBdLmN0bDAwX0NvbnRlbnRJbmZvX0NoZWNraW5mbGlnaHRzdGF0dXNfT3JpZ2luX3R4dE9yaWdpbi52YWx1ZT10aGlzLnZhbHVlO2QWAGQCEA8WBB4NV2F0ZXJtYXJrVGV4dAUERnJvbR8MZ2QCCQ9kFgoCBw9kFgICAQ8WAh8CBaMBQ2l0eSBvciA8YSBocmVmPSJqYXZhc2NyaXB0Ok9wZW5BaXJwb3J0cyh0aGlzLCdjdGwwMF9Db250ZW50SW5mb19DaGVja2luZmxpZ2h0c3RhdHVzX0Rlc3RpbmF0aW9uX3R4dERlc3RpbmF0aW9uJywnRGVzdGluYXRpb25BaXJwb3J0Jyk7IiB0YWJpbmRleD0iLTEiPmFpcnBvcnQ8L2E\x2BOmQCCQ8QDxYCHw1nZGQWAGQCDQ9kFgICAg8WDB8HZx8IZx8JAtwLHwoC\x2BgEfCwUFZW4tVVMfDGdkAg8PEA8WAh8NZxYCHw4Fb2phdmFzY3JpcHQ6ZG9jdW1lbnQuZm9ybXNbMF0uY3RsMDBfQ29udGVudEluZm9fQ2hlY2tpbmZsaWdodHN0YXR1c19EZXN0aW5hdGlvbl90eHREZXN0aW5hdGlvbi52YWx1ZT10aGlzLnZhbHVlO2QWAGQCEQ8WBB8PBQJUbx8MZ2QCCw8PFgIfBQVIZG9jdW1lbnQuZm9ybXNbMF0uYWN0aW9uPSdodHRwOi8vd3d3LnVuaXRlZC5jb20vd2ViL2VuLVVTL0RlZmF1bHQuYXNweCc7ZGQCCw8PFgIfBmhkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WFQUYY3RsMDAkQ3VzdG9tZXJIZWFkZXIkcmQxBRhjdGwwMCRDdXN0b21lckhlYWRlciRyZDIFGGN0bDAwJEN1c3RvbWVySGVhZGVyJHJkMwUcY3RsMDAkQ3VzdG9tZXJIZWFkZXIkY2hrU2F2ZQUpY3RsMDAkQ29udGVudEluZm8kQm9va2luZzEkcmRvU2VhcmNoVHlwZTEFKWN0bDAwJENvbnRlbnRJbmZvJEJvb2tpbmcxJHJkb1NlYXJjaFR5cGUyBSljdGwwMCRDb250ZW50SW5mbyRCb29raW5nMSRyZG9TZWFyY2hUeXBlMgUuY3RsMDAkQ29udGVudEluZm8kQm9va2luZzEkTmVhcmJ5YWlyJGNoa0ZsdE9wdAUsY3RsMDAkQ29udGVudEluZm8kQm9va2luZzEkQWx0RGF0ZSRjaGtGbHRPcHQFNmN0bDAwJENvbnRlbnRJbmZvJEJvb2tpbmcxJERlcERhdGVUaW1lJHJkb0RhdGVTcGVjaWZpYwUyY3RsMDAkQ29udGVudEluZm8kQm9va2luZzEkRGVwRGF0ZVRpbWUkcmRvRGF0ZUZsZXgFMmN0bDAwJENvbnRlbnRJbmZvJEJvb2tpbmcxJERlcERhdGVUaW1lJHJkb0RhdGVGbGV4BTBjdGwwMCRDb250ZW50SW5mbyRCb29raW5nMSRTZWFyY2hCeSRyZG9zZWFyY2hieTEFMGN0bDAwJENvbnRlbnRJbmZvJEJvb2tpbmcxJFNlYXJjaEJ5JHJkb3NlYXJjaGJ5MgUwY3RsMDAkQ29udGVudEluZm8kQm9va2luZzEkU2VhcmNoQnkkcmRvc2VhcmNoYnkyBTBjdGwwMCRDb250ZW50SW5mbyRCb29raW5nMSRTZWFyY2hCeSRyZG9zZWFyY2hieTMFMGN0bDAwJENvbnRlbnRJbmZvJEJvb2tpbmcxJFNlYXJjaEJ5JHJkb3NlYXJjaGJ5MwUrY3RsMDAkQ29udGVudEluZm8kQm9va2luZzEkRGlyZWN0JGNoa0ZsdE9wdAUlY3RsMDAkQ29udGVudEluZm8kbWFuYWdlcmVzJHJkb0ZsaWdodAUiY3RsMDAkQ29udGVudEluZm8kbWFuYWdlcmVzJHJkb0NhcgUiY3RsMDAkQ29udGVudEluZm8kbWFuYWdlcmVzJHJkb0NhcqiFHdwSfzHAZicdb4ILJF7\x2BywT1':'',
	'ctl00$CustomerHeader$ddlCountries':'US',
	'ctl00$CustomerHeader$rdlang':'en-us',
	'ctl00$CustomerHeader$chkSave':'on',
	'ctl00$CustomerHeader$countryText':'',
	'ctl00$CustomerHeader$langText':'',
	'ctl00$ContentInfo$Booking1$hdnText':'Award Travel',
	'ctl00$ContentInfo$Booking1$SearchType':'rdoSearchType2',
	'ctl00$ContentInfo$Booking1$Origin$TBWE01_ClientState':'',
	'ctl00$ContentInfo$Booking1$Destination$TBWE01_ClientState':'',
	'ctl00$ContentInfo$Booking1$DepDateTime$DateFlex':'rdoDateSpecific',
	'ctl00$ContentInfo$Booking1$DepDateTime$Deptime$cboDptTime':' ',
	'ctl00$ContentInfo$Booking1$DepDateTime$MonthList1$cboMonth':'11/1/2013',
	'ctl00$ContentInfo$Booking1$DepDateTime$LengthOfStay$cboLengthOfStay':'6',
	'ctl00$ContentInfo$Booking1$RetDateTime$Retdate$txtRetDate':'mm/dd/yyyy',
	'ctl00$ContentInfo$Booking1$RetDateTime$Rettime$cboDptTime':' ',
	'ctl00$ContentInfo$Booking1$Adult$cboAdult':'1',
	'ctl00$ContentInfo$Booking1$Offercode$txtPromoCode':'',
	'ctl00$ContentInfo$Booking1$Cabins$cboCabin':'Coach',
	'ctl00$ContentInfo$Booking1$SearchBy$SearchBy':'rdosearchby2',
	'ctl00$ContentInfo$Booking1$btnSearchFlight':'Search',
	'ctl00$ContentInfo$Booking1$Pckuploc$txtOrigin':'',
	'ctl00$ContentInfo$Booking1$Returnlocdropoff$txtDestination':'Same as pick-up',
	'ctl00$ContentInfo$Booking1$Pickupdate$txtDptDate':'mm/dd/yyyy',
	'ctl00$ContentInfo$Booking1$Pickuptime$cboPickUpTime':'10:00AM',
	'ctl00$ContentInfo$Booking1$Dropoffdate$txtRetDate':'mm/dd/yyyy',
	'ctl00$ContentInfo$Booking1$Dropofftime$cboRetTime':'10:00AM',
	'ctl00$ContentInfo$Booking1$Cartype$cboCarType':'C',
	'ctl00$ContentInfo$Checkinflightstatus$Onepassconfirm$txtOPNum':'',
	'ctl00$ContentInfo$Checkinflightstatus$FlightNumber$txtFltNum':'',
	'ctl00$ContentInfo$Checkinflightstatus$cboFltDates':'11/15/2013',
	'ctl00$ContentInfo$Checkinflightstatus$Origin$txtOrigin':'',
	'ctl00$ContentInfo$Checkinflightstatus$Origin$TBWE01_ClientState':'',
	'ctl00$ContentInfo$Checkinflightstatus$Destination$txtDestination':'',
	'ctl00$ContentInfo$Checkinflightstatus$Destination$TBWE01_ClientState':'',
	'ctl00$ContentInfo$manageres$confirmationOptions':'rdoFlight',
	'ctl00$ContentInfo$manageres$ConfNum$txtPNR':'',
	'ctl00$ContentInfo$manageres$LastName$txtLName':'',
	'hiddenInputToUpdateATBuffer_CommonToolkitScripts':'1'}
	return params

def new_search_params(origin, destination, depart_date):
	params = {
		'SearchTypeMain':'oneWay',
		'Origin':origin,
		'Destination':destination,
		'Flexible':'false',
		'DepartDate':depart_date,
		'ReturnDate':'',
		'flexMonth':'9/8/2015',
		'tripLength':'6',
		'NumOfAdults':'1',
		'NumOfSeniors':'0',
		'NumOfChildren03':'0',
		'NumOfChildren02':'0',
		'NumOfChildren01':'0',
		'NumOfInfants':'0',
		'NumOfLapInfants':'0',
		'cabinType':'econ',
		'awardCabinType':'awardEcon',
		'AwardTravel':'false',
		'NonStopOnly':'false',
		'search':''
	}
	return params

def new_search_params_full(origin, destination, depart_datetime, cart_id, nonstop=False,
							search_type = None):
	''' possible search types: General, Upgrade, Award '''

	params_json = '{"Revise":false,"UnaccompaniedMinorDisclamer":false,"searchTypeMain":"oneWay","Origin":"SFO","Destination":"EWR","DepartDate":"Oct 12, 2015","ReturnDate":"Oct 12, 2015","awardTravel":false,"MaxTrips":null,"numberOfTravelers":1,"numOfAdults":1,"numOfSeniors":0,"numOfChildren03":0,"numOfChildren02":0,"numOfChildren01":0,"numOfInfants":0,"numOfLapInfants":0,"travelerCount":1,"IsUnAccompaniedMinor":false,"MilitaryTravelType":null,"MilitaryOrGovernmentPersonnelStateCode":null,"tripLength":0,"flexMonth":null,"flexMonth2":null,"SortType":null,"cboMiles":null,"cboMiles2":null,"Trips":[{"DestinationAll":false,"returnARC":null,"connections":null,"nonStopOnly":false,"nonStop":true,"oneStop":true,"twoPlusStop":true,"DepartDate":"Oct 12, 2015","ReturnDate":null,"PetIsTraveling":false,"PreferredTime":"","PreferredTimeReturn":null,"Destination":"EWR","Index":1,"Origin":"SFO","Selected":false,"FormatedDepartDate":"Mon, Oct 12, 2015","OriginCorrection":null,"DestinationCorrection":null,"OriginAll":false}],"nonStopOnly":false,"CalendarOnly":false,"InitialShop":true,"IsSearchInjection":false,"CartId":"BC8A9749-3ACF-4025-861A-6A3A596ADB7C","CellIdSelected":null,"BBXSession":null,"SolutionSetId":null,"SimpleSearch":true,"RequeryForUpsell":false,"RequeryForPOSChange":false,"ShowClassOfServiceListPreference":true,"SelectableUpgradesOriginal":null,"RegionalPremierUpgradeBalance":0,"GlobalPremierUpgradeBalance":0,"RegionalPremierUpgrades":null,"GlobalPremierUpgrades":null,"FormattedAccountBalance":null,"GovType":null,"TripTypes":1,"flexible":false,"flexibleAward":false,"FlexibleDaysAfter":0,"FlexibleDaysBefore":0,"hiddenPreferredConn":null,"hiddenUnpreferredConn":null,"carrierPref":0,"chkFltOpt":0,"portOx":0,"travelwPet":0,"NumberOfPets":0,"cabinType":0,"cabinSelection":"ECONOMY","awardCabinType":0,"FareTypes":0,"FareWheelOnly":false,"buyUpgrade":0,"offerCode":null,"TVAOfferCodeLastName":null,"ClassofService":null,"UpgradeType":null,"BillingAddressCountryCode":null,"BillingAddressCountryDescription":null,"IsPassPlusFlex":false,"IsPassPlusSecure":false,"IsOffer":false,"IsMeetingWorks":false,"IsValidPromotion":false,"CalendarDateChange":null,"CoolAwardSpecials":false,"LastResultId":null,"IncludeLmx":false}'
	params = json.loads(params_json)

	# set origin
	params['Origin'] = origin
	params['Trips'][0]['Origin'] = origin
	
	# set destination
	params['Destination'] = destination
	params['Trips'][0]['Destination'] = destination
	
	# set departure date
	params['DepartDate'] = depart_datetime.strftime('%b %d, %Y')
	params['ReturnDate'] = depart_datetime.strftime('%b %d, %Y')
	params['Trips'][0]['DepartDate'] = depart_datetime.strftime('%b %d, %Y')
	params['Trips'][0]['FormatedDepartDate'] = depart_datetime.strftime('%a, %b %d, %Y')  # seriously!

	# set Cart ID
	params['CartId'] = cart_id

	# search for award or upgrade space only
	# use when expert mode is broken
	if search_type == "Upgrade":
		params['UpgradeType'] = "MUA"
	elif search_type == "Award":
		params["awardTravel"] = True

	# set nonstop parameter -- this doesn't seem to work.
	if nonstop:
		params['nonStopOnly'] = True
		params['Trips'][0]['nonStopOnly'] = True
		params["oneStop"] = False
		params["twoPlusStop"] = False

	return json.dumps(params)

def set_upgrade_params(SID):
	params = {
		'hdnServer':'.77',
		'hdnSID':SID,
		'hdnLangCode':'en-US',
		'hdnPOS':'US',
		'hdnClient':'73.162.189.4',
		'hdnInactive':'false',
		'hdnAccountNumber':'RV545571',
		'hdnAccountNumberE':'awFgN51P9moCfB0WlTuolQ%3d%3d',
		'hdnCustomerId':'55803396',
		'hdnAccountStatus':'4',
		'__EVENTTARGET':'',
		'__EVENTARGUMENT':'',
		'hdnTiming':'0.2499264 seconds',
		#'__VIEWSTATE':'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Ag8CEAIRAhICEwIUAhUCFgIXAhgCGQIaAhsCHAIdAh4CHwIgFiEQBQxOb3QgU2VsZWN0ZWQFAlhYZxAFDkFkcmlhIEFpcmxpbmVzBQJKUGcQBQ9BZWdlYW4gQWlybGluZXMFAkEzZxAFCUFpciBDaGluYQUCQ0FnEAUKQWlyIENhbmFkYQUCQUNnEAUJQWlyIEluZGlhBQJBSWcQBQ9BaXIgTmV3IFplYWxhbmQFAk5aZxAFA0FOQQUCTkhnEAUPQXNpYW5hIEFpcmxpbmVzBQJPWmcQBQhBdXN0cmlhbgUCT1NnEAUHQXZpYW5jYQUCQVZnEAUDYm1pBQJLRmcQBRFCcnVzc2VscyBBaXJsaW5lcwUCU05nEAUEQ09QQQUCQ01nEAUQQ3JvYXRpYSBBaXJsaW5lcwUCT1VnEAUIRUdZUFRBSVIFAk1TZxAFEkV0aGlvcGlhbiBBaXJsaW5lcwUCRVRnEAUHRVZBIEFpcgUCQlJnEAUFTGFjc2EFAkxSZxAFE0xPVCBQb2xpc2ggQWlybGluZXMFAkxPZxAFCUx1ZnRoYW5zYQUCTEhnEAUVU2NhbmRpbmF2aWFuIEFpcmxpbmVzBQJTS2cQBRFTaGVuemhlbiBBaXJsaW5lcwUCWkhnEAUSU2luZ2Fwb3JlIEFpcmxpbmVzBQJTUWcQBRVTb3V0aCBBZnJpY2FuIEFpcndheXMFAlNBZxAFB1NwYW5haXIFAkpLZxAFBVN3aXNzBQJMWGcQBQxUQU0gTWVyY29zdXIFAlBaZxAFBFRBQ0EFAlRBZxAFDFRBUCBQb3J0dWdhbAUCVFBnEAUEVGhhaQUCVEdnEAUQVHVya2lzaCBBaXJsaW5lcwUCVEtnEAUGVW5pdGVkBQJVQWdkZAI7D2QWBAIBD2QWAgIGD2QWAmYPFgQeC29ubW91c2VvdmVyBf4BamF2YXNjcmlwdDpTaG93RGl2KCdjdGwwMF9Db250ZW50SW5mb191Y1JlY29yZExvY2F0b3Jfc3BhblBldFNhZmVQTlJIb3ZlcicsJycpO3Bvc2l0aW9uU2F0ZWxpdGUoR2V0RWxlbWVudCgnY3RsMDBfQ29udGVudEluZm9fdWNSZWNvcmRMb2NhdG9yX3NwYW5QZXRTYWZlUE5SJyksR2V0RWxlbWVudCgnY3RsMDBfQ29udGVudEluZm9fdWNSZWNvcmRMb2NhdG9yX3NwYW5QZXRTYWZlUE5SSG92ZXInKSwgZmFsc2UsIDAsIDApO3JldHVybiBmYWxzZTseCm9ubW91c2VvdXQFXGphdmFzY3JpcHQ6U2hvd0RpdignJywnY3RsMDBfQ29udGVudEluZm9fdWNSZWNvcmRMb2NhdG9yX3NwYW5QZXRTYWZlUE5SSG92ZXInKTtyZXR1cm4gZmFsc2U7ZAIDDxBkDxYcZgIBAgICAwIEAgUCBgIHAggCCQIKAgsCDAINAg4CDwIQAhECEgITAhQCFQIWAhcCGAIZAhoCGxYcEAUOQWRyaWEgQWlybGluZXMFAkpQZxAFD0FlZ2VhbiBBaXJsaW5lcwUCQTNnEAUKQWlyIENhbmFkYQUCQUNnEAUJQWlyIENoaW5hBQJDQWcQBQlBaXIgSW5kaWEFAkFJZxAFD0FpciBOZXcgWmVhbGFuZAUCTlpnEAUDQU5BBQJOSGcQBQ9Bc2lhbmEgQWlybGluZXMFAk9aZxAFCEF1c3RyaWFuBQJPU2cQBQdBdmlhbmNhBQJBVmcQBRFCcnVzc2VscyBBaXJsaW5lcwUCU05nEAUQQ3JvYXRpYSBBaXJsaW5lcwUCT1VnEAUIRUdZUFRBSVIFAk1TZxAFEkV0aGlvcGlhbiBBaXJsaW5lcwUCRVRnEAUHRVZBIEFpcgUCQlJnEAUFTGFjc2EFAkxSZxAFE0xPVCBQb2xpc2ggQWlybGluZXMFAkxPZxAFCUx1ZnRoYW5zYQUCTEhnEAUVU2NhbmRpbmF2aWFuIEFpcmxpbmVzBQJTS2cQBRFTaGVuemhlbiBBaXJsaW5lcwUCWkhnEAUSU2luZ2Fwb3JlIEFpcmxpbmVzBQJTUWcQBRVTb3V0aCBBZnJpY2FuIEFpcndheXMFAlNBZxAFBVN3aXNzBQJMWGcQBQRUQUNBBQJUQWcQBQxUQU0gTWVyY29zdXIFAlBaZxAFDFRBUCBQb3J0dWdhbAUCVFBnEAUEVGhhaQUCVEdnEAUQVHVya2lzaCBBaXJsaW5lcwUCVEtnZGQCPQ8WAh8DBQ1kaXNwbGF5Om5vbmU7ZAI/D2QWBgIBD2QWBgIID2QWAgIBDxYCHglpbm5lcmh0bWwFhAEoY2l0eSBvciA8YSBocmVmPSJqYXZhc2NyaXB0Ok9wZW5BaXJwb3J0cyh0aGlzLCdjdGwwMF9Db250ZW50SW5mb191Y09yaWdpbjFfdHh0T3JpZ2luJywnT3JpZ2luQWlycG9ydCcpOyIgdGFiaW5kZXg9Ii0xIj5haXJwb3J0PC9hPilkAgwPZBYCAgIPFgweDUVuYWJsZUNhY2hpbmdnHg1Vc2VDb250ZXh0S2V5Zx4SQ29tcGxldGlvblNldENvdW50AtwLHhJDb21wbGV0aW9uSW50ZXJ2YWwC%2BgEeCkNvbnRleHRLZXkFBWVuLVVTHgdFbmFibGVkZ2QCDg8QDxYCHgtfIURhdGFCb3VuZGcWAh4Ib25jaGFuZ2UFVGphdmFzY3JpcHQ6ZG9jdW1lbnQuZm9ybXNbMF0uY3RsMDBfQ29udGVudEluZm9fdWNPcmlnaW4xX3R4dE9yaWdpbi52YWx1ZT10aGlzLnZhbHVlO2QWAGQCAw9kFggCBw9kFgICAQ8WAh8HBZMBKGNpdHkgb3IgPGEgaHJlZj0iamF2YXNjcmlwdDpPcGVuQWlycG9ydHModGhpcywnY3RsMDBfQ29udGVudEluZm9fdWNEZXN0aW5hdGlvbjFfdHh0RGVzdGluYXRpb24nLCdEZXN0aW5hdGlvbkFpcnBvcnQnKTsiIHRhYmluZGV4PSItMSI%2BYWlycG9ydDwvYT4pZAIJDxAPFgIfDmdkZBYAZAIND2QWAgICDxYMHwhnHwlnHwoC3AsfCwL6AR8MBQVlbi1VUx8NZ2QCDw8QDxYCHw5nFgIfDwVeamF2YXNjcmlwdDpkb2N1bWVudC5mb3Jtc1swXS5jdGwwMF9Db250ZW50SW5mb191Y0Rlc3RpbmF0aW9uMV90eHREZXN0aW5hdGlvbi52YWx1ZT10aGlzLnZhbHVlO2QWAGQCBQ9kFgICBA8PFgQeDE1pbmltdW1WYWx1ZQUJNy8xMy8yMDE1HgxNYXhpbXVtVmFsdWUFCTYvMTQvMjAxNmRkAkEPFgIfAwUNZGlzcGxheTpub25lO2QCQw9kFgYCAQ9kFgYCCA9kFgICAQ8WAh8HBYQBKGNpdHkgb3IgPGEgaHJlZj0iamF2YXNjcmlwdDpPcGVuQWlycG9ydHModGhpcywnY3RsMDBfQ29udGVudEluZm9fdWNPcmlnaW4yX3R4dE9yaWdpbicsJ09yaWdpbkFpcnBvcnQnKTsiIHRhYmluZGV4PSItMSI%2BYWlycG9ydDwvYT4pZAIMD2QWAgICDxYMHwhnHwlnHwoC3AsfCwL6AR8MBQVlbi1VUx8NZ2QCDg8QDxYCHw5nFgIfDwVUamF2YXNjcmlwdDpkb2N1bWVudC5mb3Jtc1swXS5jdGwwMF9Db250ZW50SW5mb191Y09yaWdpbjJfdHh0T3JpZ2luLnZhbHVlPXRoaXMudmFsdWU7ZBYAZAIDD2QWCAIHD2QWAgIBDxYCHwcFkwEoY2l0eSBvciA8YSBocmVmPSJqYXZhc2NyaXB0Ok9wZW5BaXJwb3J0cyh0aGlzLCdjdGwwMF9Db250ZW50SW5mb191Y0Rlc3RpbmF0aW9uMl90eHREZXN0aW5hdGlvbicsJ0Rlc3RpbmF0aW9uQWlycG9ydCcpOyIgdGFiaW5kZXg9Ii0xIj5haXJwb3J0PC9hPilkAgkPEA8WAh8OZ2RkFgBkAg0PZBYCAgIPFgwfCGcfCWcfCgLcCx8LAvoBHwwFBWVuLVVTHw1nZAIPDxAPFgIfDmcWAh8PBV5qYXZhc2NyaXB0OmRvY3VtZW50LmZvcm1zWzBdLmN0bDAwX0NvbnRlbnRJbmZvX3VjRGVzdGluYXRpb24yX3R4dERlc3RpbmF0aW9uLnZhbHVlPXRoaXMudmFsdWU7ZBYAZAIFD2QWAgIEDw8WBB8QBQk3LzEzLzIwMTUfEQUJNi8xNC8yMDE2ZGQCRQ9kFgRmDw8WAh4PVmFsaWRhdGlvbkdyb3VwZWRkAgIPDxYCHxJlZGQCCw8PFgIfAmhkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBAUYY3RsMDAkQ3VzdG9tZXJIZWFkZXIkcmQxBRhjdGwwMCRDdXN0b21lckhlYWRlciRyZDIFGGN0bDAwJEN1c3RvbWVySGVhZGVyJHJkMwUcY3RsMDAkQ3VzdG9tZXJIZWFkZXIkY2hrU2F2ZS5yi4vMs9zMxKCgUX1ok3urBHN7',
		'ctl00$CustomerHeader$ddlCountries':'US',
		'ctl00$CustomerHeader$rdlang':'en-us',
		'ctl00$CustomerHeader$chkSave':'on',
		'ctl00$CustomerHeader$countryText':'',
		'ctl00$CustomerHeader$langText':'',
		'ctl00$CustomerHeader$txtSiteSearch':'Type in keyword',
		'ctl00$ContentInfo$ucFname1$txtFName':'David',
		'ctl00$ContentInfo$ucLname1$txtLName':'Freeman',
		'ctl00$ContentInfo$ucTktNum1$txtTktNum':'',
		'ctl00$ContentInfo$ddlFFPAirlines1':'XX',
		'ctl00$ContentInfo$ucFFNum1$txtOPNum':'',
		'ctl00$ContentInfo$ucFname2$txtFName':'',
		'ctl00$ContentInfo$ucLname2$txtLName':'',
		'ctl00$ContentInfo$ucTktNum2$txtTktNum':'',
		'ctl00$ContentInfo$ddlFFPAirlines2':'XX',
		'ctl00$ContentInfo$ucFFNum2$txtOPNum':'',
		'ctl00$ContentInfo$ucFname3$txtFName':'',
		'ctl00$ContentInfo$ucLname3$txtLName':'',
		'ctl00$ContentInfo$ucTktNum3$txtTktNum':'',
		'ctl00$ContentInfo$ddlFFPAirlines3':'XX',
		'ctl00$ContentInfo$ucFFNum3$txtOPNum':'',
		'ctl00$ContentInfo$ucFname4$txtFName':'',
		'ctl00$ContentInfo$ucLname4$txtLName':'',
		'ctl00$ContentInfo$ucTktNum4$txtTktNum':'',
		'ctl00$ContentInfo$ddlFFPAirlines4':'XX',
		'ctl00$ContentInfo$ucFFNum4$txtOPNum':'',
		'ctl00$ContentInfo$ucRecordLocator$txtPNR':'8N5DOE',
		'ctl00$ContentInfo$ddlAirlines':'SQ',
		'ctl00$ContentInfo$ucOrigin1$txtOrigin':'BLR',
		'ctl00$ContentInfo$ucOrigin1$TBWE01_ClientState':'',
		'ctl00$ContentInfo$ucDestination1$txtDestination':'SIN',
		'ctl00$ContentInfo$ucDestination1$TBWE01_ClientState':'',
		'ctl00$ContentInfo$ucDepartDate1$txtDptDate':'10/30/2015',
		'ctl00$ContentInfo$ucFltnum1$txtFltNum':'503',
		'ctl00$ContentInfo$ddlCabin1':'Economy',
		'ctl00$ContentInfo$ucOrigin2$txtOrigin':'',
		'ctl00$ContentInfo$ucOrigin2$TBWE01_ClientState':'',
		'ctl00$ContentInfo$ucDestination2$txtDestination':'',
		'ctl00$ContentInfo$ucDestination2$TBWE01_ClientState':'',
		'ctl00$ContentInfo$ucDepartDate2$txtDptDate':'mm/dd/yyyy',
		'ctl00$ContentInfo$ucFltnum2$txtFltNum':'',
		'ctl00$ContentInfo$ddlCabin2':'Economy',
		'ctl00$ContentInfo$ucEmail$txtEmail':'dfreeman@cs.stanford.edu',
		'ctl00$ContentInfo$btnSubmit':'Search for upgrade availability',
		'ctl00$ContentInfo$hdfErrorNum':'',
		'hiddenInputToUpdateATBuffer_CommonToolkitScripts':'1'
	}
	return params

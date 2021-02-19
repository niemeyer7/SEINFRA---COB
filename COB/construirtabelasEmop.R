library(tidyverse)
library(foreign)
library(dplyr)
setwd("C:\\Users\\oscar.ribeiro\\Desktop\\SEINFRA---COB\\COB")

x = read.csv2('dadosgerais.csv', fileEncoding = "UTF-8")

categoria = x$categoria
familia = x$familia
item = x$item
categoria = as.data.frame(categoria)
duplicados <- duplicated(categoria,fromLast = TRUE)

categorialimpa = categoria[!duplicados,]  
categorialimpa = as.data.frame(categorialimpa)
familia = as.data.frame(familia)
duplicados <- duplicated(familia,fromLast = TRUE)
familialimpa = familia[!duplicados,]  
familialimpa = as.data.frame(familialimpa)
item = as.data.frame(item)
duplicados <- duplicated(item,fromLast = TRUE)
itemlimpa = item[!duplicados,]  
itemlimpa = as.data.frame(itemlimpa)

write.csv2(categorialimpa,"C:\\Users\\oscar.ribeiro\\Desktop\\SEINFRA---COB\\COB\\categoriaEmop.csv",fileEncoding = "UTF-8", row.names = FALSE) 
write.csv2(familialimpa,"C:\\Users\\oscar.ribeiro\\Desktop\\SEINFRA---COB\\COB\\familiaEmop.csv",fileEncoding = "UTF-8", row.names = FALSE) 
write.csv2(itemlimpa,"C:\\Users\\oscar.ribeiro\\Desktop\\SEINFRA---COB\\COB\\itemEmop.csv",fileEncoding = "UTF-8", row.names = FALSE) 

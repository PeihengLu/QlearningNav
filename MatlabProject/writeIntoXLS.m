function writeIntoXLS(time,table)
if roundn(time,0)==time && mod(time,1000)==0
    xlswrite('qtable.csv', table); 
end
end


function writeIntoXLS(time,table)
if roundn(time,0)==time && mod(time,10)==0
    xlswrite('qtable.csv', table); 
end
end


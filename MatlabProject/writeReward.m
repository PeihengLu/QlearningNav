function writeReward(time,table)
if roundn(time,0)==time && mod(time,1000)==0
    xlswrite('rewards.csv', table); 
end
end
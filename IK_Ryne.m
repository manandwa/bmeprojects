function [H,K,A] = IK_Ryne(X,Y)

    Xh = 160;
    Yh = 410;
    l1 = 122;
    l2 = 142;
    l3 = sqrt((X - Xh).^2 + (Y - Yh).^2);
    K = acos((l3.^2 - l1^2 - l2^2)./(-2*l1*l2));
    K = acosd((l3.^2 - l1^2 - l2^2)./(-2*l1*l2));
    H1 = acosd((l2^2 - l1^2 - l3.^2)./(-2*l1.*l3));
    H2 = abs(atand((X - Xh)./(Y - Yh)));
    H = 180 - H2 - H1;
    A2 = abs(atand((Y - Yh)./(X - Xh)));
    A1 = acosd((l1^2 - l2^2 - l3.^2)./(-2*l2.*l3));
    A = 180 - A1 - A2;
% 
%     fid = fopen('angles.csv','w+');
%     fprintf(fid,'%s\n','Calculated Hip,Calculated Knee,Calculated Angle');
%     pData = [H,K,A];
%     dlmwrite('angles.csv',pData,'-append');
end

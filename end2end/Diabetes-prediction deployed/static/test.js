function drawLine(x1,y1,x2,y2) {
    const dx=x2-x1;
    const dy=y2-y1;
    const dist=Math.sqrt(dx*dx+dy*dy);
    if(dist<maxDistance) {
    ctx.strokeStyle = 'rgba(255, 255, 255,${lineOpacity * (1 - dist / maxDistance)})';
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
    }
}
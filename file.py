unction onEdit(e) {                                                                                                                                      
     const range = e.range;                                                                                                                                  
     const sheet = range.getSheet();                                                                                                                         
     if (sheet.getName() !== "Leads") return;                                                                                                                
                                                                                                                                                             
     const row = range.getRow();                                                                                                                             
     if (row === 1) return; // header                                                                                                                        
                                                                                                                                                             
     // Only trigger when Status is set to "New"                                                                                                             
     const statusCol = 6; // F                                                                                                                               
     if (range.getColumn() !== statusCol) return;                                                                                                            
                                                                                                                                                             
     const status = sheet.getRange(row, statusCol).getValue();                                                                                               
     if (String(status).toLowerCase() !== "new") return;                                                                                                     
                                                                                                                                                             
     const name = sheet.getRange(row, 2).getValue();   // B                                                                                                  
     const email = sheet.getRange(row, 3).getValue();  // C                                                                                                  
     const phone = sheet.getRange(row, 4).getValue();  // D                                                                                                  
     const source = sheet.getRange(row, 5).getValue(); // E                                                                                                  
                                                                                                                                                             
     const settings = sheet.getParent().getSheetByName("Settings");                                                                                          
     const agentName = settings.getRange("B1").getValue() || "Agent";                                                                                        
     const area = settings.getRange("B2").getValue() || "your area";                                                                                         
     const notifyEmail = settings.getRange("B3").getValue();                                                                                                 
                                                                                                                                                             
     const now = new Date();                                                                                                                                 
     sheet.getRange(row, 1).setValue(now); // Timestamp                                                                                                      
                                                                                                                                                             
     const followUp = `Hi ${name || "there"} — thanks for reaching out about buying/selling in ${area}.                                                      
   When’s a good time today for a quick chat?                                                                                                                
   — ${agentName}`;                                                                                                                                          
                                                                                                                                                             
     // Put message into column J                                                                                                                            
     sheet.getRange(row, 10).setValue(followUp);                                                                                                             
                                                                                                                                                             
     // Set Next Follow-up to 2 hours later                                                                                                                  
     const next = new Date(now.getTime() + 2 * 60 * 60 * 1000);                                                                                              
     sheet.getRange(row, 8).setValue(next); // H                                                                                                             
                                                                                                                                                             
     // Optional email notification (only if email is provided)                                                                                              
     if (notifyEmail) {                                                                                                                                      
       const subject = `New Lead (Speed-to-Lead): ${name || "Unknown"} - ${source || "Unknown source"}`;                                                     
       const body =                                                                                                                                          
         `A new lead was marked NEW.\n\n` +                                                                                                                  
         `Name: ${name}\nEmail: ${email}\nPhone: ${phone}\nSource: ${source}\n\n` +                                                                          
         `Suggested follow-up:\n${followUp}\n\n` +                                                                                                           
         `Next follow-up: ${next}\n`;                                                                                                                        
       MailApp.sendEmail(notifyEmail, subject, body);                                                                                                        
     }                                                                                                                                                       
   }                           
package ch05_pjt_01.contact.service;

import ch05_pjt_01.contact.ContactSet;
import ch05_pjt_01.contact.dao.ContactDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import javax.annotation.Resource;

public class ContactSearchService {

    @Autowired
    @Qualifier("usedDao")
    private ContactDao contactDao;

//    @Autowired
//    public ContactSearchService(ContactDao contactDao) {
//        System.out.println("ContactSearchService ContactDao 파라미터로 받는 생성자 호출됨");
//        System.out.println("contactDao: " + contactDao); 	// contactDao 출력
//        this.contactDao = contactDao;
//    }

    public ContactSet searchContact(String name) {
        if (verify(name)) {
            return contactDao.select(name);
        } else {
            System.out.println("Contact information is available.");
        }

        return null;
    }

    public boolean verify(String name) {
        ContactSet contactSet = contactDao.select(name);
        return contactSet != null ? true : false;
    }

    public void setContactDao(ContactDao contactDao) {
        this.contactDao = contactDao;
    }

}

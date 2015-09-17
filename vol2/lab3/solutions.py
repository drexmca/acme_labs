# name this file 'solutions.py'
"""Volume II Lab 3: Public Key Encryption (RSA)
Donald Rex McArthur
Sept. 17, 2015
Math 320
"""
import rsa_tools as rsa

# Problem 1: Implement the following RSA system.
def EA(a,b):
    '''
    Consise recursive function that returns the gcd, and the two elements
    for the eucledian algorithm
    '''
    a = long(a)
    b = long(b)
    if a%b == 0:
        return b,0,1
    else:
        c, d, e = EA(b, a%b)
        return c, e, d-e*(a//b)


class myRSA(object):
    """RSA String Encryption System. Do not use any external modules except for
    'rsa_tools' and your implementation of the Extended Euclidean Algorithm.
    
    Attributes:
        public_key (tup): the RSA key that is available to everyone, of the
            form (e, n). Used only in encryption.
        _private_key (tup, hidden): the secret RSA key, of the form (d, n).
            Used only in decryption.
    
    Examples:
        >>> r = myRSA()
        >>> r.generate_keys(1000003,608609,1234567891)
        >>> print(r.public_key)
        (1234567891, 608610825827)
        
        >>> r.decrypt(r.encrypt("SECRET MESSAGE"))
        'SECRET MESSAGE'
        
        >>> s = myRSA()
        >>> s.generate_keys(287117,104729,610639)
        >>> s.decrypt(r.encrypt("SECRET MESSAGE",s.public_key))
        'SECRET MESSAGE'
    """

    def __init__(self):
        """Initialize public and private key variables."""
        self.public_key = None
        self._private_key = None
        self.n = None
    
    def generate_keys(self, p, q, e):
        """Create a pair of RSA keys.
        
        Inputs:
            p (int): A large prime.
            q (int): A second large prime .
            e (int): The encryption exponent. 
        
        Returns:
            Set the public_key and _private_key attributes.
        """
        n = p*q
        phi_n = (p-1)*(q-1) 
        gcd, d_prime, temp = EA(e,phi_n)
        d = d_prime % phi_n
        self.public_key = (e,n)
        self._private_key = (d,n)
        pass
    
    def encrypt(self, message, key=None):
        """Encrypt 'message' with a public key and return its encryption as a
        list of integers. If no key is provided, use the 'public_key' attribute
        to encrypt the message.
        
        Inputs:
            message (str): the message to be encrypted.
            key (int tup, opt): the public key to be used in the encryption.
                 Defaults to 'None', in which case 'public_key' is used.
        """
        if key == None:
            key = long(self.public_key[0])
        key = long(key)
        #print key
        n = long(self.public_key[1])
        m_int = []
        for x in message:
            x = rsa.string_to_int(x)
            m_int.append(x)
        encrypt = []
        for i in m_int:
            c = pow(long(i),long(key),long(n))
            encrypt.append(c)
        return encrypt
    
    def decrypt(self, ciphertext):
        """Decrypt 'ciphertext' with the private key and return its decryption
        as a single string. You may assume that the format of 'ciphertext' is
        the same as the output of the encrypt() function. Remember to strip off
        the fill value used in rsa_tools.partition().
        """
        m_dec = []
        for i in ciphertext:
            m_prime = long(i)**long(self._private_key[0]) % long(self._private_key[1])
            m_dec.append(m_prime)
        m_str = []
        string = str()
        for x in m_dec:
            a = rsa.int_to_string(x)
            string += a
        string = string.rstrip('~')
        return string



# Problem 2: Partially test the myRSA class with this function.
#   Use Exceptions to indicate inappropriate arguments or test failure.
def test_myRSA(message, p, q, e):
    """Create a 'myRSA' object. Generate a pair of keys using 'p', 'q', and
    'e'. Encrypt the message, then decrypt the encryption. If the decryption
    is not exactly the same as the original message, raise a ValueError with
    error message "decrypt(encrypt(message)) failed."
    
    If 'message' is not a string, raise a TypeError with error message
    "message must be a string."
    
    If any of p, q, or e are not integers, raise a TypeError with error
    message "p, q, and e must be integers."
    
    Inputs:
        message (str): a message to be encrypted and decrypted.
        p (int): A large prime for key generation.
        q (int): A second large prime for key generation.
        e (int): The encryption exponent.
        
    Returns:
        True if no exception is raised.
    """
    if type(message) != str:
        raise TypeError("Your message must be a string")
    if type(p)!=int or type(q) !=int or type(e) != int:
        raise TypeError("p,q,e must be a int")
    r = myRSA()
    r.generate_keys(p,q,e)
    m_split = rsa.partition(message, rsa.string_size(r.public_key[1]),'~')
    m_enc = r.encrypt(m_split)
    string = r.decrypt(m_enc)
    print string
    if string != message:
        raise ValueError("decrypt(encrypt(message)) failed.")
    return True

test_myRSA('HELLLO', 443, 449, 457)
#test_myRSA('A', 1000003,608609,1234567891)

# Problem 3: Fermat's test for primality.
def is_prime(n):
    """Use Fermat's test for primality to see if 'n' is probably prime.
    Run the test at most five times, using integers randomly chosen from
    [2, n-1] as possible witnesses. If a witness number is found, return the
    number of tries it took to find the witness. If no witness number is found
    after five tries, return 0.
    
    Inputs:
        n (int): the candidate for primality.
    
    Returns:
        The number of tries it took to find a witness number, up to 5
        (or 0 if no witnesses were found).
    
    """
    raise NotImplementedError("Problem 3 incomplete.")


# Problem 4: Implement the following RSA system using PyCrypto.
class PyCrypto(object):
    """RSA String Encryption System. Do not use any external modules except for
    those found in the 'Crypto' package.
    
    Attributes:
        _keypair (RSA obj, hidden): the RSA key (both public and private).
            Facilitates encrypt() and decrypt().
        public_key (str): A sharable string representation of the public key.
    
    Examples:
        
        >>> p = PyCrypto()
        >>> p.decrypt(p.encrypt("SECRET MESSAGE"))
        'SECRET MESSAGE'
        
        >>> print(p.public_key)
        -----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQ...
        ...
        ...HwIDAQAB
        -----END PUBLIC KEY-----
        
        >>> q = PyCrypto()
        >>> q.decrypt(p.encrypt("SECRET MESSAGE",q.public_key))
        'SECRET MESSAGE'
    
    """
    def __init__(self):
        """Initialize the _keypair and public_key attributes."""
        raise NotImplementedError("Problem 4 incomplete.")
    
    def encrypt(self, message, key=None):
        """Encrypt 'message' with a public key and return its encryption. If
        no key is provided, use the '_keypair' attribute to encrypt 'message'.
        
        Inputs:
            message (str): the message to be encrypted.
            key (str, opt): the string representation of the public key to be
                used in the encryption. Defaults to 'None', in which case
                '_keypair' is used to encrypt the message.
        """
        raise NotImplementedError("Problem 4 incomplete.")
    
    def decrypt(self, ciphertext):
        """Decrypt 'ciphertext' with '_keypair' and return the decryption."""
        raise NotImplementedError("Problem 4 incomplete.")

# ============================== END OF FILE ============================== #

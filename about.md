# CommandLine
Version: 0.0.3

## Notices:
- The first time you start up CL you must use the default account.

## Known bugs:
- Users with admin can create a account higher than their own (admin is rank level 2 or above)
- Attempting to log in with an invalid username creates an error with location of users lines
- Users other than the last user the file cannot log in

## Major changes:
-

## Bug fixes:
- When using logout, the system now does a full reset.
- Multiple users can no longer have the same username.
- Users can no longer su into an account that doesn't exist
- When using su, the rank of the session no longer stays the same as before the switch.

## CLib changes:
- Added userExists(user, [file]) to determine if a user is in the users file, returns a boolean
- Added userParams(user, [file]) to retreive user's parameters, returns a list, [password, rank]
- Changed the hash feature to be slightly faster

## Clib bug fixes:
- 

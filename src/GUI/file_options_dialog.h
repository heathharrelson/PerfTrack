//! \file file_options_dialog.h
// John May, 27 January 2005

/*****************************************************************
* PerfTrack Version 1.0 (September 2005)
* 
* For information on PerfTrack, please contact John May
* (johnmay@llnl.gov) or Karen Karavanic (karavan@cs.pdx.edu).
* 
* See COPYRIGHT AND LICENSE information at the end of this file.
*
*****************************************************************/

//! Defines a dialog for setting text file read/write options

#ifndef FILE_OPTIONS_DIALOG_H
#define FILE_OPTIONS_DIALOG_H

#include <qstring.h>

#include "file_options_dialog_base.h"

class FileOptionsDialog : public FileOptionsDialogBase {
	Q_OBJECT
public:
	FileOptionsDialog( QWidget * parent = 0, const char * name = 0 );

	//! Returns the chosen column separator string
	QString colSep() const;
	//! Returns the chosen row separator string
	QString rowSep() const;
	//! Returns the chosen file extensionstring (with leading .)
	QString fileExtension() const;
	//! Returns setting for including hidden lines
	bool includeHidden() const;
public slots:
	//! Set the indicated row separator.  Does not affect the
	//! default file extension (as clicking the button would)
	void setRowSep( QString sep );

	//! Set the indicated col separator.  Does not affect the
	//! default file extension (as clicking the button would)
	void setColSep( QString sep );

	//! Set the indicated file extension. 
	void setFileExtension( QString sep );

	//! Set the indicated "include hidden" flag
	void setIncludeHidden( bool includeHidden );

protected slots:
	//! Sets a default entry for the file extension based on
	//! the current setting of the column and row separators.
	//! The parameter is ignored; it's needed for compatibility
	//! with the signals connected to it.
	void setDefaultExtension( int );

	//! Clicks the column Other radio button when \a text is not
	//! empty.  Does nothing if \a text is empty.
	void setColOtherButton( const QString& );

	//! Clicks the row Other radio button when \a text is not
	//! empty.  Does nothing if \a text is empty.
	void setRowOtherButton( const QString& );
};
#endif

/****************************************************************************
COPYRIGHT AND LICENSE
 
Copyright (c) 2005, Regents of the University of California and
Portland State University.  Produced at the Lawrence Livermore
National Laboratory and Portland State University.
UCRL-CODE-2005-155998
All rights reserved.
 
Redistribution and use in source and binary forms, with or
without modification, are permitted provided that the following
conditions are met:
 
* Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in
the documentation and/or other materials provided with the
distribution.
* Neither the name of the University of California
or Portland State Univeristy nor the names of its contributors
may be used to endorse or promote products derived from this
software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

ACKNOWLEDGMENT

1. This notice is required to be provided under our contract with the U.S.
Department of Energy (DOE).  This work was produced at the University
of California, Lawrence Livermore National Laboratory under Contract
No. W-7405-ENG-48 with the DOE.

2. Neither the United States Government nor the University of California
nor any of their employees, makes any warranty, express or implied, or
assumes any liability or responsibility for the accuracy, completeness, or
usefulness of any information, apparatus, product, or process disclosed, or
represents that its use would not infringe privately-owned rights.

3.  Also, reference herein to any specific commercial products, process, or
services by trade name, trademark, manufacturer or otherwise does not
necessarily constitute or imply its endorsement, recommendation, or
favoring by the United States Government or the University of California.
The views and opinions of authors expressed herein do not necessarily
state or reflect those of the United States Government or the University of
California, and shall not be used for advertising or product endorsement
purposes. 
****************************************************************************/

